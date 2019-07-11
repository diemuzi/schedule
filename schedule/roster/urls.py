from django.urls import path

from schedule.roster import views

app_name = 'roster'

urlpatterns = [
    path('edit/<int:pk>', views.Profile.as_view(), name='edit'),

    path('download', views.Download.as_view(), name='download')
]
