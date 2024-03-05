from django.urls import path
from . import views

app_name = 'x'

urlpatterns = [
    path('', views.index, name="home"),
    path('movie/<int:movie_id>/', views.detail, name="detail")
]