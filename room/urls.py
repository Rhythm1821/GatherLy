from django.urls import path
from . import views

app_name = "room"

urlpatterns = [
    path("create-room/",views.create_room,name="create-room"),
    path("search/", views.search, name="search"),
    path('delete-room/<str:room_id>/',views.delete_room,name="delete-room"),
    path('delete-member/<str:room_id>/',views.delete_member,name="delete-member"),
    path('all-members/<str:room_id>/',views.all_members,name="all-members"),
    path("<str:room_id>/",views.room,name="room"),
]


# Rhythm422@
