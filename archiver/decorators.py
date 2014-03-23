from django.contrib.auth.forms import AuthenticationForm as auth_form
from django.core.context_processors import csrf

def dashboard_view(view):
    def inner(request, *args, **kwargs):
        context = {'request': request, 'user': request.user}
        if not request.user.is_active:
            context['form'] = auth_form(request)
            context['next'] = '/dashboard'
            context.update(csrf(request))
        kwargs['context'] = context
        return view(request, *args, **kwargs)
    return inner
