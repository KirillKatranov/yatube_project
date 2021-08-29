from django.urls import path

from . import views
app_name = 'post'

urlpatterns = [
    path('', views.index, name = 'main_page'),
    path('group/<slug:slug>/', views.group_posts, name = 'gr_post')
] 