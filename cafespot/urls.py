from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.lista_cafenele, name='lista_cafenele'),
    path('cafe/<int:cafe_id>/', views.detalii_cafenea, name='detalii_cafenea'),
    path('cafe/<int:cafe_id>/favorit/', views.toggle_favorit, name='toggle_favorit'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='cafespot/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('favorite/', views.lista_favorite, name='lista_favorite'),
]