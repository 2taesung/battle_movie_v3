from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import User, UserSerializer

@api_view(['POST'])
def signup(request):
    # 1. 사용자한테 아이디, 비밀번호를 받아서
    # username = request.data.get('username')
    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')

    if password != password_confirmation:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    # 2. (바인딩 후 ) 유효성 검사를 하고
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # 3. 저장(== 회원가입)
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(data=serializer.data)