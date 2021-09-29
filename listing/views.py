from rest_framework import generics, permissions
from .models import Home
from .serializers import HomeSerializer
from django.shortcuts import render


# get/post
# is auth or read only, you can browse but if you want to make
# changes you have to sign in
class HomeListings(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = HomeSerializer

# update/delete/patch


class SingleHome(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = HomeSerializer
