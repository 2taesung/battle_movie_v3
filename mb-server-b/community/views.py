#PEP8 이라는 파이썬 암묵적 준수하는 스타일 가이드가 있다.
#내장 모듈

#외부 라이브러리
from django.shortcuts import get_object_or_404
# import community
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#장고
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


#커스텀 파일 or 로컬 파일
from .serializers import *
from .models import *
from accounts.serializers import *
from accounts.models import *
# from community import serializers
User = get_user_model()


# Create your views here.
@api_view(['POST'])
def post_create(request):
    movie1_title = request.data.get('movie_title_1')
    movie2_title = request.data.get('movie_title_2')
    movie1 = Movie.objects.get(title=movie1_title)
    movie2 = Movie.objects.get(title=movie2_title)
    if request.user.is_authenticated:
        # print()
        if request.method == 'POST':
            serializer = CommunitySerializer(data = request.data)
            # print(serializer)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, movie_title_1=movie1, movie_title_2=movie2)
                return Response(serializer.data)
        return Response(status=400)
    return Response(status=400)


#무비 리스트 불러오기
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies= Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = CommunitySerializer(data=request.data) # 바인딩
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(author=request.user)
    #         return Response(data=serializer.data, status=status.HTTP_201_CREATED)


#게시글 리스트 불러오기
@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts= Community.objects.all()
        serializer = CommunitySerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommunitySerializer(data=request.data) # 바인딩
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def community_list(request):
#     if request.method == 'GET':
#         movies= Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CommunitySerializer(data=request.data) # 바인딩
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(author=request.user)
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, post_id):
    post = get_object_or_404(Community, pk=post_id)
    if request.method == 'GET':
        serializer = CommunitySerializer(post)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        # 바인딩
        serializer = CommunitySerializer(
                data=request.data, instance=post
                )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#내가 적은 or 투표한 글(?)
@api_view(['GET'])
def my_post(request):
    user = request.user
    user_serializer = UserSerializer(user)
    return Response(user_serializer.data)


#프로필
@api_view(['GET'])
def profile(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    user_serializer = UserSerializer(user)
    return Response(user_serializer.data)
