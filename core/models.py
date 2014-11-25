from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import encrypted_fields


class TestModel(models.Model):
    test_field = encrypted_fields.EncryptedIntegerField(
        blank=True, null=True
    )
