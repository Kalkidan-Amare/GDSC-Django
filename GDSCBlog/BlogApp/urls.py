from django.urls import path
from . import views

app_name = 'BlogApp'

urlpatterns = [
    path('',views.blog_fun)
]