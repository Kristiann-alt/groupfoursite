from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
        #Gender 
    path('gender/list', login_required(views.gender_list), name='gender_list'),
    path('gender/add', login_required(views.add_gender), name='add_gender'),
    path('gender/edit/<int:genderId>', login_required(views.edit_gender), name='edit_gender'),
    path('gender/delete/<int:genderId>', login_required(views.delete_gender), name='delete_gender'),

        #User
    path('user/list', login_required(views.user_list), name='user_list'),
    path('user/add', login_required(views.add_user), name='add_user'),
    path('user/edit/<int:userId>/', login_required(views.edit_user), name='edit_user'),
    path('user/delete/<int:userId>/', login_required(views.delete_user), name='delete_user'),
    path('user/change_password/<int:userId>', login_required(views.change_password), name='change_password'),

        #Authentication
    path('', views.login_view, name='login'),
    path('logout/',  views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home, name='home'),
]