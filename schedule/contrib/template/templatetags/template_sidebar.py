from django import template

register = template.Library()


@register.simple_tag(takes_context=True, name='template_sidebar')
def sidebar(context, namespace):
    """
    Side Bar

    Set's active and white text color on sidebar if it's currently active.

    :param dict context: Context
    :param str|list namespace: Name of namespace

    :return: str
    """

    request = context.get('request')

    if ',' in namespace:
        namespace = namespace.split(',')
    else:
        namespace = namespace.strip()

    if type(namespace) is list and request.resolver_match.namespace in namespace:
        return 'text-white'
    elif type(namespace) is str and request.resolver_match.namespace == namespace.lower():
        return 'text-white'
