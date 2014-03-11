from django_nav import nav_groups, Nav, NavOption
from django_nav.conditionals import user_is_authenticated

class ArchiverNav(Nav):
    """
        This is a primary Navigation link, Most apps should only define one of these
        If the application truly wants to have Navigation links for all of their landing pages
        They can use the NavOption and have the main Nav with their Home state
    """
    name = u'ACM Archiver'
    view = 'archiver.views.dashboard'
    dashboard = True
    icon = 'cog'
    nav_group = 'main'

nav_groups.register(ArchiverNav)
