# Generated by Django 3.0 on 2020-03-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200330_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='registration',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
