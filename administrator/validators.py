import magic
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validateFileMimeType(file):
    accept = ['applications/pdf']
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if file_mime_type not in accept:
        raise ValidationError(_('Unsupported file type'), code='invalid')
