from django.core.exceptions import PermissionDenied

def register_applicant_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_register_applicant():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view

def register_recruiter_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_register_recruiter():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return _wrapped_view
