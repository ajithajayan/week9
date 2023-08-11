from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('adminpage/',views.adminpage,name='adminpage'),
    path('delete/<int:row_id>/', views.delete_row, name='delete_row'),
    path('edit/<int:row_id>/', views.edit_row, name='edit_row'),
]