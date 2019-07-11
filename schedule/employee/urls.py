from django.urls import path

from schedule.employee import views

app_name = 'employee'

urlpatterns = [
    path('add', views.Add.as_view(), name='add'),

    path('delete/<int:pk>', views.Delete.as_view(), name='delete'),

    path('edit/<int:pk>', views.Profile.as_view(), name='edit'),

    path('password', views.Password.as_view(), name='password'),

    path('', views.Search.as_view(), name='search')
]
