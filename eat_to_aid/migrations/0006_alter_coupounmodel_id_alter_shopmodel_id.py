# Generated by Django 5.0.1 on 2024-01-11 05:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eat_to_aid', '0005_alter_coupounmodel_id_alter_shopmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupounmodel',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('cbe30797-ec30-53f2-8015-7acad1f4c9c7'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='shopmodel',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('c7ddfee4-2d86-5bdc-8842-fdfd01b28093'), primary_key=True, serialize=False, unique=True),
        ),
    ]
