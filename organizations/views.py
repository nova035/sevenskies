from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from organizations.models import Organization, OrganizationContact
from organizations.serializer import OrganizationSerializer, OrganizationContactSerializer


class OrganizationView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetailView(RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationContactView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = OrganizationContact.objects.all()
    serializer_class = OrganizationContactSerializer


class OrganizationContactDetailView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = OrganizationContact.objects.all()
    serializer_class = OrganizationContactSerializer