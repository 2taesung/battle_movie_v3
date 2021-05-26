from django.urls import path
from . import views

urlpatterns = [
    # todo list
    path('profile/<int:user_pk>/', views.profile),
    # GET http://localhost:8000/api/v1/community/
    path('movie_list/', views.movie_list),
    path('post_list/', views.post_list),

    # GET, POST, PUT, DELETE http://localhost:8000/api/v1/community/:id/
    path('post_detail/<int:post_id>/', views.post_detail),
    # test
    # path('json-1/', views.community_json_1),
    path('post_create/', views.post_create),
    path('my_post/', views.my_post, name='my_post'),

]
