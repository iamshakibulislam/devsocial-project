# Generated by Django 3.2.2 on 2021-05-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210508_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preprintdetails',
            name='type_available_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='preprintdetails',
            name='type_available_link_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
