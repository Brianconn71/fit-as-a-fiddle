from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    User profile form for storing default delivery info
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Below adds placeholders and classes, removes auto-generated labels
        and sets the autofocus to the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_1': 'Street Address 1',
            'default_street_2': 'Street Address 2',
            'default_county': 'County',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = f'border \
                                                         rounded-2 \
                                                         profile-form-input'
            self.fields[field].label = False
