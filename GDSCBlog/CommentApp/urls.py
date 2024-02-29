from django.urls import path
from . import views

app_name = 'CommentApp'

urlpatterns = [
    path('',views.comment_fun),
]