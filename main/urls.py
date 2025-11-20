from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.header, name="header_page"),  # Главная страница
    path('index/', views.index, name="index_page"),
    path('owner/<int:id>/', views.detail, name="detail_page"),
    path('login/', views.login_view, name="login_page"),
    path('register/', views.register, name="register_page"),
    path('profile/', views.profile, name="profile_page"),
    path('logout/', views.logout_view, name="logout_page"),

    #path('c_based_template/', views.MyTemplateView.as_view(), name="c_based_temp_page"),
]