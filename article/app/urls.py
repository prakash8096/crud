
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.Data.as_view(),name='home'),
    path('detail/<int:pk>', views.Detail.as_view(),name='detail'),
    path('create/', views.Create.as_view(),name='create'),
    path('Update/<int:pk>', views.Update.as_view(),name='edit'),
    path('Delete/<int:pk>', views.Delete.as_view(),name='delete'),
   
]
