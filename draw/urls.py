from django.urls import path
from . import views

urlpatterns = [
    path('',views.reg,name='reg'),
    path('login/', views.logi, name='login'),
    path('create/', views.create_design, name='create_design'),
    path('edit/<int:design_id>/', views.edit_design, name='edit_design'),
]
