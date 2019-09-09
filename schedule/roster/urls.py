from django.urls import path

from schedule.roster import views

app_name = 'roster'

urlpatterns = [
    path('download', views.Download.as_view(), name='download'),

    path('edit/<int:pk>', views.Profile.as_view(), name='edit'),

    path('preview/all', views.PreviewAll.as_view(), name='preview-all'),

    path('preview/<int:pk>/employee', views.PreviewEmployee.as_view(), name='preview-employee')
]
