import re

from django.core.exceptions import ValidationError


class OnlyDigitsValidator:

    def __call__(self, value):
        pattern = r'^[0-9]{1,15}$'
        matches = re.findall(pattern, value)
        if not matches:
            raise ValidationError

    def deconstruct(self):
        return (
            'main_app.validators.OnlyDigitsValidator',
            (),
            {}
        )

