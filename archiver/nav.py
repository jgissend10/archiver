from django_nav import nav_groups, Nav, NavOption

class SubOption(NavOption):
    """
    This is an Option of an Option, this can go on for the max
    recursion depth of python (Further then you want to try and go)
    """
    name = u'Sub Option'
    view = 'archiver.views.dashboard'

class TestOption(NavOption):
    """
        This is a Navigation Option, which can be used to build drop down menus
    """
    name = u'Test Option'
    view = ''
    options = [SubOption]

class TestNav(Nav):
    """
        This is a primary Navigation link, Most apps should only define one of these
        If the application truly wants to have Navigation links for all of their landing pages
        They can use the NavOption and have the main Nav with their Home state
    """
    name = u'First Test Nav'
    view = ''
    nav_group = 'main'
    options = [TestOption]

nav_groups.register(TestNav)