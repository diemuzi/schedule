from django.contrib.auth.views import LogoutView
from django.urls import path

from login import views

app_name = 'login'

urlpatterns = [
    path('', views.Index.as_view(redirect_authenticated_user=True), name='login'),

    path('create', views.Create.as_view(), name='create'),

    path('logout', LogoutView.as_view(), name='logout'),

    path('password', views.Password.as_view(), name='password'),

    path('<int:pk>/delete', views.Delete.as_view(), name='delete')
]
