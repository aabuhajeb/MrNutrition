import django_filters
from django_filters import CharFilter

from .models import *

class ProductFilter(django_filters.FilterSet):
    name_product = CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = Product
        fields = '__all__'
        exclude = [   'user','name',
            'image',
            'price',
            'digital',
            'ptype',
            'flavor',
            'manufacture',
            'food_type',
            'food_flavor',
            'food_manufacture',
            'description',
            'rating',
            'numReviews',
            'countInStock',
            'createdAt',
        ]
        