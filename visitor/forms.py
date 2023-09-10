import requests
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import BaseUserCreationForm, UsernameField, PasswordResetForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import User

UserModel = get_user_model()


class CustomUserCreationForm(BaseUserCreationForm):
    url_sendinblue = "https://api.brevo.com/v3/smtp/email"

    class Meta:
        model = User
        fields = ('user_username', 'user_email', 'user_phone_number', 'user_address', 'password1', 'password2')
        field_classes = {"user_username": UsernameField}

    def clean_username(self):
        """Reject usernames that differ only in case."""
        username = self.cleaned_data.get("username")
        if (
                username
                and self._meta.model.objects.filter(username__iexact=username).exists()
        ):
            self._update_errors(
                ValidationError(
                    {
                        "username": self.instance.unique_error_message(
                            self._meta.model, ["username"]
                        )
                    }
                )
            )
        else:
            return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user


class SendInBluePasswordResetForm(PasswordResetForm):
    url_sendinblue = "https://api.brevo.com/v3/smtp/email"
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "email",
                "class": "form-control",
                "placeholder": "name@example.com"
            }
        ),
    )

    def email_sendinblue(
            self,
            subject_template_name,
            email_template_name,
            context,
            from_email,
            to_email,
            html_email_template_name=None,
    ):
        headers = {
            "accept": "application/json",
            "api-key": settings.API_KEY_SENDINBLUE,
            "content-type": "application/json"
        }

        subject = render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = "".join(subject.splitlines())

        payload = {
            "sender": {
                "name": "Si Garang",
                "email": "noreply@mail.com"
            },
            "to": [
                {"email": to_email, "sender": "Sender"}
            ],
            "subject": subject,
            "htmlContent": render_to_string(email_template_name, context)
        }

        response = requests.request("POST", self.url_sendinblue, json=payload, headers=headers)

    def save(
            self,
            domain_override=None,
            subject_template_name="registration/password_reset_subject.txt",
            email_template_name="registration/password_reset_email.html",
            use_https=False,
            token_generator=default_token_generator,
            from_email=None,
            request=None,
            html_email_template_name=None,
            extra_email_context=None,
    ):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        email = self.cleaned_data["email"]
        if not domain_override:
            current_site = get_current_site(request)
            site_name = current_site.name
            domain = current_site.domain
        else:
            site_name = domain = domain_override
        email_field_name = UserModel.get_email_field_name()
        for user in self.get_users(email):
            user_email = getattr(user, email_field_name)
            context = {
                "email": user_email,
                "domain": domain,
                "site_name": site_name,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                "token": token_generator.make_token(user),
                "protocol": "https" if use_https else "http",
                **(extra_email_context or {}),
            }
            self.email_sendinblue(
                subject_template_name,
                email_template_name,
                context,
                from_email,
                user_email,
                html_email_template_name=html_email_template_name,
            )
