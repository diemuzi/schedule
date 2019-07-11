from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

register = template.Library()

# Navigation Array
nav = []


@register.simple_tag(takes_context=True, name='template_breadcrumb')
def breadcrumb(context):
    """
    Breadcrumb

    :param dict context: Context

    :return: str
    """

    request = context.get('request')

    html = ''

    for item in nav:
        if item.get('namespace') == request.resolver_match.namespace:
            html += '<li class="breadcrumb-item">' + _(item.get('label')) + '</li>'

            for page in item.get('pages'):
                if page.get('url_name') == request.resolver_match.url_name:
                    html += '<li class="breadcrumb-item">' + _(page.get('label')) + '</li>'

    return mark_safe(html)


@register.simple_tag(takes_context=True, name='template_title')
def title(context):
    """
    Title

    :param dict context: Context

    :return: str
    """

    request = context.get('request')

    html = ''

    for item in nav:
        if item.get('namespace') == request.resolver_match.namespace:
            html += ' : ' + _(item.get('label'))

            for page in item.get('pages'):
                if page.get('url_name') == request.resolver_match.url_name:
                    html += ' : ' + _(page.get('label'))

    return mark_safe(html)
