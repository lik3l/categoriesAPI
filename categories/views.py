from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Category
from . import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = dict(
        default=serializers.CategorySerializer,
        list=serializers.SimpleCategorySerializer,
        retrieve=serializers.RetrieveSerializer
    )

    def get_queryset(self):
        qs = super(CategoryViewSet, self).get_queryset()
        if self.action == 'retrieve':
            return qs.select_related('parent').prefetch_related('children')
        return qs

    def get_serializer_class(self):
        return self.serializer_class['default'] \
            if self.action not in self.serializer_class \
            else self.serializer_class[self.action]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        resp = super(CategoryViewSet, self).retrieve(request, *args, **kwargs)
        return resp
