from django.forms import DateTimeInput
from django.utils.translation import gettext_lazy as _
from django_filters import FilterSet, DateTimeFilter, CharFilter


class FeedbackFilter(FilterSet):
    title = CharFilter(
        field_name='feedbackPost__title',
        lookup_expr='icontains',
        label='Post title'
    )
    date = DateTimeFilter(
            field_name='date_create',
            lookup_expr='gt',
            label=_('Date creation'),
            widget=DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local'},
            )
        )


