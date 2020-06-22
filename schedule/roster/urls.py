from django.urls import path

from roster import views

app_name = 'roster'

urlpatterns = [
    path('', views.Search.as_view(), name='search'),

    path('download', views.Download.as_view(), name='download'),

    path('preview', views.PreviewAll.as_view(), name='preview-all'),

    path('<int:pk>/preview', views.PreviewEmployee.as_view(), name='preview-employee'),

    path('<int:pk>/profile', views.Profile.as_view(), name='profile'),

    path('<int:pk>/schedule', views.Schedule.as_view(), name='schedule')
]
