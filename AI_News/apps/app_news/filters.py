from rest_framework import generics
from django_filters import rest_framework as filters
from .models import News


class NewsFilter(filters.FilterSet):
    min_id = filters.NumberFilter(field_name="id", lookup_expr='gte')
    max_id = filters.NumberFilter(field_name="id", lookup_expr='lte')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = News
        fields = ['title', 'min_id', 'max_id']
