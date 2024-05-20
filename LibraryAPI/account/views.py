from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializer import *
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'message': 'Logout successful!'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)

        data={}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registered Successfully!'
            data['username'] = account.username
            data['email'] = account.email
            data['password'] =account.password
        #token auth
            # token=Token.objects.get(user=account).key
            # data['token'] = token
        # JWT
            token = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(token),
                'access':str(token.access_token)
            }
        else:
            data=serializer.errors
        return Response(data)
