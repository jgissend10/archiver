from django import template
from django.template import Template, Variable, TemplateSyntaxError

register = template.Library()

@register.simple_tag(takes_context=True)
def render_as_template(context, variable):
    t = Template(variable)
    return t.render(context)
