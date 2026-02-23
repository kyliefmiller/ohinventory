import django_filters
from .models import OHEntry
from django.db.models import Q

def get_choices_for_field(model, field_name):
    def get_choices():
        all_values = model.objects.values_list(field_name, flat=True)
        unique_values = set()
        
        for entry in all_values:
            if entry:
                for v in entry.split(','):
                    unique_values.add(v.strip())
        
        return [(v, v) for v in sorted(unique_values)]
    return get_choices

class EntryFilter(django_filters.FilterSet):

    institution = django_filters.ChoiceFilter(choices=OHEntry.Institution.choices, lookup_expr='exact', empty_label='Any')
    medium = django_filters.MultipleChoiceFilter(
        choices=get_choices_for_field(OHEntry, 'medium'),
        method='filter_by_comma_separated'
    )
    access = django_filters.MultipleChoiceFilter(
        choices=get_choices_for_field(OHEntry, 'access'),
        method='filter_by_comma_separated'
    )
    narrator = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.MultipleChoiceFilter(
        choices=get_choices_for_field(OHEntry, 'location'),
        method='filter_by_comma_separated'
    )
    topic = django_filters.MultipleChoiceFilter(
        choices=get_choices_for_field(OHEntry, 'topic'),
        method='filter_by_comma_separated'
    )
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = OHEntry
        fields = ['institution', 'medium', 'access', 'narrator', 'location', 'topic','description']
# 'year'
       

    def filter_by_comma_separated(self, queryset, name, value):
            if not value:
             return queryset
        
            query = Q()
            for v in value:
                query |= Q(**{f'{name}__icontains': v})
        
            return queryset.filter(query)