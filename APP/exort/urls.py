from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('food/', views.food),
    path('place/', views.place),
    path('create_card/', views.create_card),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete')
]
