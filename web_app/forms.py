from django.forms import CharField, Form, PasswordInput

class CityForm(Form):
    """Form for user to add city to API request."""
    city = CharField(label='Enter a city', max_length=100)

class LoginForm(Form):
    """Form for user to log in."""
    username = CharField(label='username: ', max_length=100)
    password = CharField(label='password: ', max_length=100, widget=PasswordInput())