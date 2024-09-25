from django.urls import path,include
from .import views

urlpatterns = [
   path('',views.home,name='home'),
   path('login/',views.login_view,name='login'),
   path('logout/',views.logout_view,name='logout'),
   path('register/',views.register_view,name='register'),
   path('register/',views.register_view,name='register'),
   path('dashboard/<username>/',views.dashboard_view,name='dashboard'),
   path('create-order/<str:plan>/', views.create_order, name='create_order'),
   path('payment-success/', views.payment_success, name='payment_success'),
]