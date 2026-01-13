from django.shortcuts import render
from rest_framework.views import APIView
from userapi.serializer import registerSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class registerapi(APIView):

    def post(self, request):


        serilazer = registerSerializer(data = request.data)

        if serilazer.is_valid():

            serilazer.save()

            return Response(serilazer.data,status=status.HTTP_200_OK)
        
        return Response(serilazer.errors,status=status.HTTP_400_BAD_REQUEST)
    


