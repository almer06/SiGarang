import requests
from django.conf import settings
from django.template.loader import render_to_string


class SendInBlue:
    url_sendinblue = "https://api.brevo.com/v3/smtp/email"
    __API_KEY_SENDINBLUE = settings.API_KEY_SENDINBLUE
    headers = {
        "accept": "application/json",
        "api-key": __API_KEY_SENDINBLUE,
        "content-type": "application/json"
    }

    def email_sendinblue(
            self,
            subject_template_name,
            email_template_name,
            context,
            from_email,
            to_email,
            html_email_template_name=None,
    ):

        subject = render_to_string(subject_template_name, context)
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

        response = requests.request("POST", self.url_sendinblue, json=payload, headers=self.headers)
        print(response)
