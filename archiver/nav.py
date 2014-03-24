from django_nav import nav_groups, Nav, NavOption
from django_nav.conditionals import user_is_authenticated, user_is_not_authenticated

class ArchiverNav(Nav):
    """
        This is a primary Navigation link, Most apps should only define one of these
        If the application truly wants to have Navigation links for all of their landing pages
        They can use the NavOption and have the main Nav with their Home state
    """
    name = u'ACM Archiver'
    view = 'archiver.views.dashboard'
    icon = 'cog'
    nav_group = 'main'

class LoginOption(NavOption):
    name = u'Login'
    url = '/accounts/login/'
    template = 'django_nav/topoption.html'
    conditional = {'function': user_is_not_authenticated, 'args': [],
                               'kwargs': {}}

class LogoutOption(NavOption):
    name = u'Logout'
    url = '/accounts/logout/'
    template = 'django_nav/topoption.html'
    conditional = {'function': user_is_authenticated, 'args': [],
                               'kwargs': {}}

class UserTopNav(Nav):
    name = u'Welcome {{ user }} ' 
    icon = 'user'
    nav_group = 'top'
    template = 'django_nav/topnav.html'
    options = [LoginOption, LogoutOption]

nav_groups.register(UserTopNav)
nav_groups.register(ArchiverNav)
