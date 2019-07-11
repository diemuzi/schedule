from django.contrib.auth.views import LogoutView
from django.urls import path

from schedule.login import views

app_name = 'login'

urlpatterns = [
    path('', views.Index.as_view(), name='login'),

    path('logout', LogoutView.as_view(), name='logout')
]
