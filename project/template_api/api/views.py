from __future__ import absolute_import
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import TemplateSnippet
from .serializers import TemplateSnippetDefaultSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly, UserSerializerPermissions


@api_view(('GET',))
@permission_classes((IsAuthenticatedOrReadOnly,))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        'register': reverse('register', request=request, format=format)
    })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserSerializerPermissions,)


class TemplateSnippetList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = TemplateSnippet.objects.all()
    serializer_class = TemplateSnippetDefaultSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TemplateSnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )
    queryset = TemplateSnippet.objects.all()
    serializer_class = TemplateSnippetDefaultSerializer

