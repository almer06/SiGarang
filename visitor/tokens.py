from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp) -> str:
        user_pk = six.text_type(user.pk)
        timestamp = six.text_type(timestamp)
        user_email = six.text_type(user.user_email)
        user_active = six.text_type(user.is_active)

        return f"{user_pk}{timestamp}{user_email}{user_active}"


activation_account = AccountActivationTokenGenerator()
