import django_filters

from issue.models import Issue
from podcast.models import Podcast

CHOICES = (
    ('ascending', 'Ascending'),
    ('descending', 'Descending')
)


class IssueFilter(django_filters.FilterSet):
    publishing_date = django_filters.DateFilter(label='Publishing Date')
    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Issue
        fields = {
            'name': ['icontains'],
            'subject': ['icontains'],
        }

    def filter_by_order(self, queryset, name, value):
        expression = 'download_count' if value == 'ascending' else '-download_count'
        return queryset.order_by(expression)


class PodcastFilter(django_filters.FilterSet):
    publishing_date = django_filters.DateFilter(label='Publishing Date')
    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

    class Meta:
        model = Podcast
        fields = {
            'name': ['icontains'],
        }

    def filter_by_order(self, queryset, name, value):
        expression = 'download_count' if value == 'ascending' else '-download_count'
        return queryset.order_by(expression)
