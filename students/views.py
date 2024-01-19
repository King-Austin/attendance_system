from django.shortcuts import render, redirect
from django.contrib.auth import views as authViews
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from . models import Student
from django.contrib.auth.decorators import login_required


# Create your views here.

#@login_required(login_url='/login')
def dashboard(request):
    if request.user.is_authenticated:   
        ref = Student.objects.get(reg_number=request.user).sex
        sex = {'M':'male'}.get(ref)

    else:
        sex = 'M'
    return render(request, template_name='dashboard.html', context={'sex':sex})

    
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
                
                elif User.objects.filter(email=email).exists():
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

def userProfile(request):
    ref = Student.objects.get(reg_number=request.user).sex
    sex = {'M':'male'}.get(ref)

    return render(request, template_name='profile.html', context={'sex':sex})
    
def userSetting(request):
    ref = Student.objects.get(reg_number=request.user).sex
    sex = {'M':'male'}.get(ref)

    return render(request, template_name='setting.html', context={'sex':sex})

def forgotPassword(request):
    
    return render(request, template_name='forgot.html')

@login_required()
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
            message = 'Password Update Successful! Login here'
            messages.success(request, message)
            logout(request)
            return redirect('login')

        else:
            message = 'Password Mismatch, try again'
            messages.warning(request, message)
            return redirect ('setting')
    else:
        return redirect('setting')

@login_required()
def editProfile(request):

    pass

def passwordResetDone(request):
    pass


    