from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls import re_path

from schedule.login import views

app_name = 'login'

urlpatterns = [
    path('', views.Index.as_view(redirect_authenticated_user=True), name='login'),

    re_path(r'^access'
            r'(?:/page/(?P<page>[0-9]+))?'
            r'$',
            views.Access.as_view(), name='access'),

    path('logout', LogoutView.as_view(), name='logout'),

    path('create', views.Create.as_view(), name='create')
]
