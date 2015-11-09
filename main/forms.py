from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.bootstrap import FormActions
from django.contrib.auth.forms import UserCreationForm, UserChangeForm  
from main.models import CustomUser

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
    #args are variables, key-word arguments are variables and a value
    #val, val2='something'
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/contact/'
        
        self.helper.layout = Layout(
            Div('name', 'email', 'phone', css_class="col-md-6"),
            Div('message', css_class="col-md-6")
            )

        self.helper.layout.append(
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary', style='margin-top:30px'),
                ),
            )

class UserLogin(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class UserSignUp(forms.Form): 
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class CustomUserCreationForm(UserCreationForm):  
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CustomUser
        fields = ['email']
        exclude = ['username']


class CustomUserChangeForm(UserChangeForm):  
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CustomUser
        fields = []


# class ArtistSearchForm(forms.Form):
#     name=forms.CharField(required=False)
#     # <form action="/artists_list/" method='GET'>
#     #     <input name='artist_name' type='text' size='15' placeholder='Search for an artist' style="width: 30%; font-size:20px; text-align:center; margin: 0 auto">
#     #     </form>

#     def __init__(self, *args, **kwargs):
#         super(ArtistSearchForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_action = '/artists_list/'
#         self.helper.layout.append(
#             FieldWithButtons('field_name', StrictButton("Go!"))
#             )