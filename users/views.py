from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import CustomUserSerializer
from users.models import CustomUser


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_class = CustomUser
    ordering_fields = ('first_name', 'last_name', 'email', 'username',)


class UserDetailView(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class MeView(APIView):

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)