from django.shortcuts import render, redirect
from django.contrib.auth import views as authViews
from attendance.models import Attendance
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from . models import Student
from .decorators import login_required


# Create your views here.

@login_required
def dashboard(request):
    student = Student.objects.get(reg_number=request.user)
    sex = {'M':'male'}.get(student.sex) # the need for the profile picture
    attendance = Attendance.objects.filter(active=True).order_by('start_date')

    return render(request, template_name='dashboard.html', context={'sex':sex, 'attendances':attendance})

    
# ======== Register Student view ==================================#

def registerView(request):
    if request.method == 'POST':
        # user registration process
        # --- Obtaining POST parameters -->
        username = request.POST['regnumber']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        birth_date = request.POST['bdate']
        
        #--- Verify the regnumber for the student -- > 
        
        reg_valid = Student.objects.filter(reg_number=username).exists()
        if reg_valid:

            #-- Verify Password match --> #
            if password == repassword:
                if User.objects.filter(username=username).exists():
                    messages.warning(request, 'Regnumber Already Exists.')
                    return redirect('register')
                
                elif User.objects.filter(email__iexact=email).exists():
                    messages.warning(request, 'Email Address Already Exists.')
                    return redirect('register')
                
                else:
                    # registration
                    ## Fetch the initial names record from the database
                    # then save along in the User models
                    stu = Student.objects.get(reg_number=username)
                    first_name, last_name = stu.first_name, stu.last_name
                    stu.birth_date = birth_date

                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    #-- Save the new and the Edited records of the students -- #
                    user.save()
                    stu.save()

                    messages.success(request, 'Registration Successful! login to your account.')
                    return redirect('login')
            else:
                messages.warning(request, 'Passwords do not match.')
                return redirect('register')
        else:
            # is user not among the the Regnumber list
            messages.warning(request, 'Sorry, student record absent')
            return redirect('register')
    # if none of the above is applied.- new session    
    else:
        return render(request, template_name='register.html')
    
##==========================================================##

def loginView(request):
    if request.method == 'POST':
        username = request.POST['regnumber']
        password = request.POST['password']

    
        user = authenticate(username=username,
                            password=password,
                            )
        # if user exist in the User database
        if user is not None:
            login(request, user)
            return redirect('dashboard')
            
        else:
            error_message = 'Invalid regnumber or Password'
            messages.warning(request, error_message)
            return redirect('login')
    else:
        
        return render(request, 'login.html',)

# --Defining the logout page for the user -- #

def logoutView(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect ('login')

@login_required
def userProfile(request):
    student = Student.objects.get(reg_number=request.user)
    sex = {'M':'male'}.get(student.sex)

    return render(request, template_name='profile.html', context={'sex':sex, 'student':student})

@login_required  
def userSetting(request):
    student = Student.objects.get(reg_number=request.user)
    sex = {'M':'male'}.get(student.sex)
    return render(request, template_name='setting.html', context={'sex':sex, 'student':student})

@login_required
def passwordChange(request):
    user = request.user
    if request.method == 'POST':
        repassword = request.POST['repassword']
        password = request.POST['password']

        #Validating Password Match
        if password == repassword:
            ref = User.objects.get(username=user)
            ref.set_password(password)
            ref.save()
            message = 'Password Update Successful! Login'
            messages.success(request, message)
            logout(request)
            return redirect('login')

        else:
            message = 'Password Mismatch, try again'
            messages.warning(request, message)
            return redirect ('setting')
    else:
        return redirect('setting')

@login_required 
def editProfile(request):

    if request.method == 'POST':
        authcode = request.POST['authcode']
        email = request.POST['email']
        bdate = request.POST['bdate']
        phone = request.POST['phone']

        try:
            user = User.objects.get(username=request.user)
            student = Student.objects.get(reg_number=request.user)
            user.email = email
            student.auth_code, student.birth_date, student.phone, = authcode, bdate, phone

            user.save()
            student.save()
            message = 'Profile Update Successful!'
            messages.success(request, message)
            
            return redirect('setting')

        except:
            message = 'Something went wrong!'
            messages.warning(request, message)
            return redirect ('setting')
    else:
        return redirect('setting')



def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']

        try:
            user = User.objects.get(email=email)

            message = 'A reset link has been sent to your email!'
            messages.success(request, message)
            
            return redirect('login')

        except:
            message = 'No account registered with given email'
            messages.warning(request, message)
            return redirect ('setting')
        
    return render(request, template_name='forgot.html')

def passwordResetDone(request):
    pass


    