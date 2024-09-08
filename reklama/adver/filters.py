import django_filters
from .models import Adver


class AdverFilter(django_filters.FilterSet):
    start_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    end_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    price_type = django_filters.CharFilter(field_name='price_type', lookup_expr='icontains')
    street = django_filters.CharFilter(field_name='street__name', lookup_expr='icontains')

    class Meta:
        model = Adver
        fields = ['start_price', 'end_price','price_type']
