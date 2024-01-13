import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendance_system.settings")
django.setup()


from students.models import Student as stu

def save_student_record(reg, first, last, sex):
    
    student = stu.objects.create(reg_number = reg,
                  first_name = first,
                  last_name = last,
                  sex = sex
                  )
    #Save the student record to the database

   


def import_record(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader) ## To skip the header row
        i = 0
        for row in reader:
            reg_number = int(row[0])
            first_name = row[1].strip().upper()
            last_name = row[2].strip().upper()
            sex = row[4].strip()
            

            save_student_record(reg_number, first_name, last_name, sex)
            
            print('Saved %s records' % (i))
            i += 1

csv_file = 'ECE_Student_Database.csv'
import_record(csv_file)
