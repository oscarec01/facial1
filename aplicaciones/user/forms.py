from django import forms
from aplicaciones.user.models import User


class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password',
                'id': 'password1',
                'required': 'required',
            }
        )
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter again your password',
                'id': 'password2',
                'required': 'required',
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'name', 'lastname', 'is_admin')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control border',
                    'placeholder': 'Email',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control border',
                    'placeholder': 'Enter your name',
                }
            ),
            'lastname': forms.TextInput(
                attrs={
                    'class': 'form-control border',
                    'placeholder': 'Enter your lastname',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control border',
                    'placeholder': 'Enter your username',
                }
            ),
            'is_admin': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input p-0',
                    'style': (
                        'weight:25px;'
                        'font-size: 110%;'
                        'display: inline;'
                        'transform: scale(1.9);'
                    )
                }
            ),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError(
                'The passwords you entered did not match!'
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
