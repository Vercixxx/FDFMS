from django.shortcuts import render
from functools import wraps
from django.http import HttpResponse

def user_not_authenticated(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse("Access denied. You don't have permission to access this page.", status=403)
        else:
            return view_func(request, *args, **kwargs)
    return wrapped_view

@user_not_authenticated
def general_logging(request):
    """
    Method call to log-in user
    """
    pass