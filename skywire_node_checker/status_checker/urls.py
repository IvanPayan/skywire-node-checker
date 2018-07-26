from django.conf.urls import url
from . import views

app_name = "online_checker"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^update/', views.update, name='update'),
    url(r'^online_uninterruptedly/', views.online_uninterruptedly, name='uninterruptedly')
]
