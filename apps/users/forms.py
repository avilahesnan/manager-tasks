from django import forms


class LoginForm(forms.Form):
    name_login = forms.CharField(
        label='Login Name',
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Ex.: João Silva'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-password',
                'placeholder': 'Enter your password'
            }
        )
    )


class RegisterForm(forms.Form):
    name_register = forms.CharField(
        label='Registration Name',
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Ex.: João Silva'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Ex.: joaosilva@gmail.com'
            }
        )
    )
    password_1 = forms.CharField(
        label='Password',
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-password',
                'placeholder': 'Enter your password'
            }
        )
    )
    password_2 = forms.CharField(
        label='Confirm your password',
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-password',
                'placeholder': 'Re-enter your password'
            }
        )
    )

    def clean_name_register(self):
        name = self.cleaned_data.get('name_register')

        if name:
            name = name.strip()
            
            if ' ' in name:
                raise forms.ValidationError('Spaces are not allowed in this field!')
            else:
                return name
            
    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')

        if password_1 and password_2:
            if password_1 != password_2:
                raise forms.ValidationError('Passwords must be the same!')
            else:
                return password_2
