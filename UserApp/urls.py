from UserApp import views
from django.urls import path
urlpatterns=[
    path('index_user/',views.index_user,name="index_user"),
    path('user_register/', views.user_register, name="user_register"),
    path('save_user_register/', views.save_user_register, name="save_user_register"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
]