from . import views
from django.urls import path, include

urlpatterns = (
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-category/', views.create_category, name='create_category'),
    path('create-fruit/', views.CreateFruitView.as_view(), name='create_fruit'),
    #path('create-fruit/', views.create_view, name='create_fruit'),
    path('<int:pk>/', include([
        path('edit-fruit/', views.edit_view, name='edit_fruit'),
        #path('delete-fruit/', views.delete_view, name='delete_fruit'),
        path('delete-fruit/', views.DeleteFruitView.as_view(), name='delete_fruit'),
        path('details-fruit/', views.details_view, name='details_fruit'),
    ]))
)