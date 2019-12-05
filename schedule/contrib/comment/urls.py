from django.urls import path

from schedule.contrib.comment import views

app_name = 'comment'

urlpatterns = [
    path('add/<int:object_id>/<str:object_name>', views.Add.as_view(), name='add')
]
