# Generated by Django 2.0 on 2018-06-13 20:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(default=1, on_delete='model', related_name='games', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
