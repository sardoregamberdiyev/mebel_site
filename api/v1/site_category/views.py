
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from sitee.models import Category
from .serializer import CategorySerializer
from .services import *


class CategoryViews(GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            root = Category.objects.get(pk=pk)
        except:
            raise NotFound("Object not found")
        return root

    def get(self, requests, *args, **kwargs):
        if 'pk' in kwargs and kwargs['pk']:
            response = get_one(kwargs['pk'])
        else:
            response = get_all(kwargs['pk'])

        return Response(response, status=HTTP_200_OK)

    def put(self, requests, *args, **kwargs):
        root = self.get_object(kwargs['pk'])
        serializer = self.get_serializer(data=requests.data, instance=root)
        serializer.is_valid(raise_exception=True)
        root = serializer.save(serializer.data)
        response = get_one(root.pk)
        return Response(response, status=HTTP_200_OK)

    def post(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        root = serializer.create(serializer.data)
        response = get_one(root.pk)
        return Response(response, status=HTTP_200_OK)
