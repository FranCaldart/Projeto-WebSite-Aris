import django_filters
from .models import NC


class NCFilter(django_filters.FilterSet):
    class Meta:
        model = NC
        fields = '__all__'
        exclude = ['Unidade','Descricao','OBS', 'latitude','longitude']
