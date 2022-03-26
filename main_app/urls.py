from django.urls import path
from . import views

#this is like app.use() in express

urlpatterns = [
    path('', views.Home.as_view(), name='home'), #here we've added the new path
    
    path('about/', views.About.as_view(), name='about'),

    path('dogs/', views.Dog_List.as_view(), name='dog_list'),

    path('dogs/new/', views.Dog_Create.as_view(), name="dog_create"),


    path('dogs/<int:pk>/', views.Dog_Detail.as_view(), name="dog_detail"),
    
    path('dogs/<int:pk>/update', views.Dog_Update.as_view(), name = 'dog_update'),

    path('dogs/<int:pk>delete', views.Dog_Delete.as_view(), name="dog_delete"),


    path('user/<username>/', views.profile, name='profile'),

    path('dogtoys/', views.dogtoys_index, name='dogtoys_index'),
    path('dogtoys/<int:dogtoy_id>', views.dogtoys_show, name='dogtoys_show'),

    path('dogtoys/create/', views.DogToyCreate.as_view(), name='dogtoys_create'),

    path('dogtoys/<int:pk>/update/', views.DogToyUpdate.as_view(), name='dogtoys_update'),

    path('dogtoys/<int:pk>/delete/', views.DogToyDelete.as_view(), name='dogtoys_delete'),
]

