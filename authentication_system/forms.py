from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class NewUserForm(UserCreationForm):
	class Meta:
		User = get_user_model()
		model = User
		fields = ("email", "username", "password1", "password2")

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)