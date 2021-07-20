from django import forms
from .models import *


class ReviewForm(forms.ModelForm):
    """ Form for users to add reviews of products"""
    class Meta:
        model = Review
        fields = ('title', 'comment', 'rating')

    def __init__(self, *args, **kwargs):
        """
        Overriding default placeholders and styles
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'comment': 'Review',
            'rating': 'Rating',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields[field].widget.attrs['class'] = 'border rounded-2 profile-form-input'
        self.fields[field].label = False