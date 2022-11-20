from django import forms
from .models import Users


class UsersForm(forms.ModelForm):
    

    class Meta:
        model = Users
        fields = ('email', 'name', 'surname', 'salary', 'phone', 'cname')
        labels = {
            'phone': 'Phone Number',
            'cname': 'Country'

        }


    def __init__(self, *args, **kwargs):
        super(UsersForm, self).__init__(*args, **kwargs)
        self.fields['cname'].empty_label = "Select"
