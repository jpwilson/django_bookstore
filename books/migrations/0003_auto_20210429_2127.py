# Generated by Django 3.1.8 on 2021-04-29 21:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_reviews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
    ]
