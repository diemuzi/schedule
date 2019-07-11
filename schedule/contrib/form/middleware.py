from django.shortcuts import redirect

from schedule.contrib.form.exceptions import FormException
from schedule.utils.redirects import json_redirect


class FormExceptionMiddleware:
    """
    Form Exception Middleware
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Execute before each request before the view

        response = self.get_response(request)

        # Execute after each request / response

        return response

    @staticmethod
    def process_exception(request, exception):
        # Used in Views
        if isinstance(exception, FormException):
            if request.method == 'POST':
                return json_redirect('home:index')
            else:
                return redirect('home:index')
