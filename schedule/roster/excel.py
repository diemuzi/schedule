import io
from collections import OrderedDict

import xlsxwriter
from django.http import HttpResponse

from roster import models


def generate_excel():
    # Create an in-memory output file for the new workbook.
    output = io.BytesIO()

    # Create a workbook.
    workbook = xlsxwriter.Workbook(output)

    # BGM page.
    bgm = workbook.add_worksheet(name='BGM')
    bgm.set_header('&CBayou Grande Marina Schedule')
    bgm.hide_gridlines(False)
    bgm.set_landscape()
    bgm.fit_to_pages(1, 0)

    # SCM page.
    scm = workbook.add_worksheet(name='SCM')
    scm.set_header('&CSherman Cove Marina Schedule')
    scm.hide_gridlines(False)
    scm.set_landscape()
    scm.fit_to_pages(1, 0)

    # Name format.
    cell_format_name = workbook.add_format({
        'align': 'left',
        'valign': 'vcenter',
        'font_color': '#000000',
        'bg_color': '#FFFFFF',
        'border': 1,
        'border_color': '#000000',
        'bold': False,
        'text_wrap': False
    })

    # Default format.
    cell_format_default = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'font_color': '#000000',
        'bg_color': '#FFFFFF',
        'border': 1,
        'border_color': '#000000',
        'bold': False,
        'text_wrap': True
    })

    # Default col settings.
    bgm.set_column(0, 7, 20, cell_format_default)
    scm.set_column(0, 7, 20, cell_format_default)

    # Header format.
    header_format = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'font_color': '#000000',
        'bg_color': '#FFFFFF',
        'border': 1,
        'border_color': '#000000',
        'bold': True,
        'text_wrap': False
    })

    # Set Headers.
    header_names = OrderedDict({
        'A1': ['Name', header_format],
        'B1': ['Friday', header_format],
        'C1': ['Saturday', header_format],
        'D1': ['Sunday', header_format],
        'E1': ['Monday', header_format],
        'F1': ['Tuesday', header_format],
        'G1': ['Wednesday', header_format],
        'H1': ['Thursday', header_format],
    })

    for key, value in header_names.items():
        bgm.write(key, value[0], value[1])
        scm.write(key, value[0], value[1])

    # Default row/col values.
    bgm_row = 1
    scm_row = 1
    col = 0

    roster = models.Roster.objects.filter(account__is_superuser=False, account__is_staff=True).order_by(
        'account__first_name')

    # Create page data.
    for item in roster:
        # Employee page.
        employee_page = workbook.add_worksheet(name=item.account.first_name + ' ' + item.account.last_name)
        employee_page.set_header('&C' + item.account.first_name + ' ' + item.account.last_name + ' Schedule')
        employee_page.hide_gridlines(False)
        employee_page.set_landscape()
        employee_page.fit_to_pages(1, 0)

        employee_page.set_column(0, 7, 20, cell_format_default)

        for key, value in header_names.items():
            employee_page.write(key, value[0], value[1])

        employee_page.write_string(1, col, item.account.first_name, cell_format_name)

        # Daily schedules.
        schedule = OrderedDict({
            'friday': {
                'set': item.is_friday,
                'col': col + 1,
                'start_time': item.start_time_friday,
                'end_time': item.end_time_friday
            },
            'saturday': {
                'set': item.is_saturday,
                'col': col + 2,
                'start_time': item.start_time_saturday,
                'end_time': item.end_time_saturday
            },
            'sunday': {
                'set': item.is_sunday,
                'col': col + 3,
                'start_time': item.start_time_sunday,
                'end_time': item.end_time_sunday
            },
            'monday': {
                'set': item.is_monday,
                'col': col + 4,
                'start_time': item.start_time_monday,
                'end_time': item.end_time_monday
            },
            'tuesday': {
                'set': item.is_tuesday,
                'col': col + 5,
                'start_time': item.start_time_tuesday,
                'end_time': item.end_time_tuesday
            },
            'wednesday': {
                'set': item.is_wednesday,
                'col': col + 6,
                'start_time': item.start_time_wednesday,
                'end_time': item.end_time_wednesday
            },
            'thursday': {
                'set': item.is_thursday,
                'col': col + 7,
                'start_time': item.start_time_thursday,
                'end_time': item.end_time_thursday
            }
        })

        # Employee name.
        if item.account.facility == 'bgm':
            bgm.write_string(bgm_row, col, item.account.first_name, cell_format_name)
        else:
            scm.write_string(scm_row, col, item.account.first_name, cell_format_name)

        # Days of Week.
        for key, value in schedule.items():
            dow = ''

            if value['set']:
                if not value['start_time'] is None and not value['end_time'] is None:
                    dow += str(value['start_time']) + ' - ' + str(value['end_time'])

            if item.account.facility == 'bgm':
                bgm.write_string(bgm_row, value['col'], dow, cell_format_default)
            else:
                scm.write_string(scm_row, value['col'], dow, cell_format_default)

            # Employee page.
            employee_page.write_string(1, value['col'], dow, cell_format_default)

        # Row counter.
        if item.account.facility == 'bgm':
            bgm_row += 1
        else:
            scm_row += 1

    # Close the workbook before sending the data.
    workbook.close()

    # Rewind the buffer.
    output.seek(0)

    # Set up the Http response.
    filename = 'Schedule.xlsx'

    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response
