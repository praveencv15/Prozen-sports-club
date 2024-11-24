from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name= 'core'

urlpatterns =[
    path('more/',views.det,name='det'),
    path('new/',views.new, name='new'),
    path('members/', views.member, name='member'),
    path('store/', views.storage, name='store'),
    path('storage/', views.storage, name='storage'),
    path('index/', views.index, name='index'),
    path('admin_dashboard/', views.admin, name='admindash'),
    path('', auth_views.LoginView.as_view(template_name="core/login.html",authentication_form=LoginForm), name="login"),
    path('logout/', views.logout, name='logout'),
    path('member/<int:member_id>/', views.member_detail, name='member_detail'),
    path('tournament/register/', views.tournament_registration, name='tournament_register'),
    path('tournament/register/success/', views.tournament_registration_success, name='tournament_registration_success'),
    path('tournament/registration/', views.tournament_registration_view, name='tournament_registration'),
    path('registration/success/', views.registration_success_view, name='registration_success'),
    path('tournament/<int:pk>/', views.tournament_detail, name='tournament_detail'),
    path("tournaments/<str:sport_name>/", views.sport_tournaments, name="sport_tournaments"),
]