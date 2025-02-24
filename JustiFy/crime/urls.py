from django.urls import path
from . import views

app_name = 'crime'

urlpatterns = [
    path('feed/', views.post_list, name='post_list'),  # or feed if you prefer
    path('create/', views.create_crime_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:pk>/vote/<str:vote_type>/', views.vote_post, name='vote_post'),
    path('post/<int:pk>/share/', views.share_post, name='share_post'),
    path('post/<int:pk>/save/', views.save_post, name='save_post'),  # if you have a save view
]
