from django.shortcuts import redirect
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from common.models import Location, Industry, ContactType, Contact
from common.serializer import (LocationSerializer, IndustrySerializer, ContactTypeSerializer, ContactSerializer)


class APIRoot(APIView):
    def get(self, request, format=None):
        return Response()


def root_redirect_view(request):
    return redirect('api:root_listing', permanent=True)


class LocationView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetailView(RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class IndustryView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class IndustryDetailView(RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class ContactTypeView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer


class ContactTypeDetailView(RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer


class ContactView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailView(RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
