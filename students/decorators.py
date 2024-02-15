from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Check if user is authenticated as a student
        if not request.user.is_authenticated:
            message = 'Kindly Authenticate'
            messages.warning(request, message)
            return redirect('login')

        # All conditions met, proceed to the view function
        return view_func(request, *args, **kwargs)

    return wrapper