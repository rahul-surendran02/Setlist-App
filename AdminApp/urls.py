from django.urls import path
from AdminApp import views
urlpatterns=[
    path('index/',views.index,name="index"),
    path('add_songs/', views.add_songs, name="add_songs"),
    path('save_songs/', views.save_songs, name="save_songs"),
    path('display_songs_admin/', views.display_songs_admin, name="display_songs_admin"),
    path('edit_songs/<int:song_id>/', views.edit_songs, name="edit_songs"),
    path('update_songs/<int:song_ID>/', views.update_songs, name="update_songs"),
    path('delete_songs/<int:del_song_ID>/', views.delete_songs, name="delete_songs"),
    path('admin_register/', views.admin_register, name="admin_register"),
    path('save_admin_register/', views.save_admin_register, name="save_admin_register"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('', views.main_page, name="main_page"),

]