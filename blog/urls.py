from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard_page, name='dashboard'),
    path('signup', views.signup_page, name='signup'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('add_post', views.add_post, name='addpost'),
    path('update_post/<int:id>', views.update_post, name='updatepost'),
    path('delete_post/<int:id>', views.delete_post, name='deletepost'),
]
