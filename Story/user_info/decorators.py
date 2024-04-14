from django.shortcuts import redirect
from functools import wraps

def login_required_or_no_access(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('main:no_access')  
        return view_func(request, *args, **kwargs)
    return wrapped_view
