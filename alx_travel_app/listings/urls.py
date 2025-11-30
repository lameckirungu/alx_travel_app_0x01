from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.listings_list, name='list'),
    path('<int:id>/', views.listing_detail, name='detail'),
    path('create/', views.listing_create, name='create'),
    path('<int:id>/update/', views.listing_update, name='update'),
    path('<int:id>/delete/', views.listing_delete, name='delete'),
]