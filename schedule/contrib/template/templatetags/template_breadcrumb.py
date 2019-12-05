from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from schedule.utils import filters

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
                if page.get('url_name') == request.resolver_match.url_name and page.get('label') is not None:
                    html += '<li class="breadcrumb-item">' + _(page.get('label')) + '</li>'

    return mark_safe(html)


@register.simple_tag(takes_context=True, name='template_meta_description')
def meta_description(context):
    """
    Meta Description

    :param dict context: Context

    :return: str
    """

    request = context.get('request')

    html = ''

    for item in nav:
        if item.get('namespace') == request.resolver_match.namespace:
            for page in item.get('pages'):
                if page.get('url_name') == request.resolver_match.url_name:
                    html += page.get('meta_description')

    return mark_safe(html)


@register.simple_tag(takes_context=True, name='template_meta_keyword')
def meta_keyword(context):
    """
    Meta Keyword

    :param dict context: Context

    :return: str
    """

    request = context.get('request')

    html = ''

    for item in nav:
        if item.get('namespace') == request.resolver_match.namespace:
            for page in item.get('pages'):
                if page.get('url_name') == request.resolver_match.url_name:
                    for keyword in page.get('meta_keywords'):
                        html += keyword + ','

    if filters.isdefined(html):
        return mark_safe(html[:-1])

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
                if page.get('url_name') == request.resolver_match.url_name and page.get('label') is not None:
                    html += ' : ' + _(page.get('label'))

    return mark_safe(html)
