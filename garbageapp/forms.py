from django import forms
from .models import Notification, userreg

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['user', 'message']

    # Override the __init__ method to customize the 'user' field
    def __init__(self, *args, **kwargs):
        super(NotificationForm, self).__init__(*args, **kwargs)
        # Customize the user field to display usernames instead of user objects
        self.fields['user'].queryset = userreg.objects.all()
        self.fields['user'].label_from_instance = lambda obj: obj.username  # Use the username field for display
