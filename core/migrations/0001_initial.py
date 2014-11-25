# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_field', encrypted_fields.fields.EncryptedIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(10000000)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
