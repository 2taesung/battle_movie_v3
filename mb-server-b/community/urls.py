from django.urls import path
from . import views

urlpatterns = [
    # todo list
    # GET http://localhost:8000/api/v1/community/
    path('', views.community_list),

    # GET, POST, PUT, DELETE http://localhost:8000/api/v1/community/:id/
    path('<int:community_id>/', views.community_detail),
    # test
    # path('json-1/', views.community_json_1),

]
