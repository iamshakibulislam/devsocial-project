# Generated by Django 3.2.2 on 2021-05-22 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210509_0544'),
    ]

    operations = [
        migrations.AddField(
            model_name='preprintdetails',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
    ]
