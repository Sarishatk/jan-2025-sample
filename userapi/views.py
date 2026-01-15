from django.shortcuts import render
from rest_framework.views import APIView
from userapi.serializer import registerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
# Create your views here.

class registerapi(APIView):

    authentication_classes = [AllowAny]


    def post(self, request):


        serilazer = registerSerializer(data = request.data)

        if serilazer.is_valid():

            serilazer.save()

            return Response(serilazer.data,status=status.HTTP_200_OK)
        
        return Response(serilazer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class loginapi(APIView):

    authentication_classes = [BasicAuthentication]

    permission_classes=[IsAuthenticated]

    def post(self, request):

        user = request.user

        token, created = Token.objects.get_or_create(user=user)

        return Response({"message":"login successfull",'token' : token.key},status=status.HTTP_200_OK)


    


