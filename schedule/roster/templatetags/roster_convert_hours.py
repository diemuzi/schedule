from datetime import datetime
from datetime import timedelta

from django import template

register = template.Library()


@register.simple_tag(name='roster_convert_hours')
def convert_hours(end_time, start_time, has_break=False):
    """
    Convert Hours

    :param int end_time: End Time
    :param int start_time: Start Time
    :param bool has_break: Has a lunch break

    :return: int
    """

    fmt = '%H:%M:%S'

    end = end_time[:2] + ':' + end_time[2:] + ':00'
    start = start_time[:2] + ':' + start_time[2:] + ':00'

    total = datetime.strptime(end, fmt) - datetime.strptime(start, fmt)

    fin = (total - timedelta(minutes=30) if has_break else total)

    if days_hours_minutes(fin)[2] > 0:
        return str(days_hours_minutes(fin)[1]) + '.' + str(days_hours_minutes(fin)[2])
    else:
        return str(days_hours_minutes(fin)[1])


def days_hours_minutes(td):
    return td.days, td.seconds // 3600, (td.seconds // 60) % 60
