from django.forms import CharField, Form, PasswordInput

class CityForm(Form):
    city = CharField(label='Enter a city', max_length=100)

class LoginForm(Form):
    username = CharField(label='username: ', max_length=100)
    password = CharField(label='password: ', max_length=100, widget=PasswordInput())