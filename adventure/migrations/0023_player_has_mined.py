# Generated by Django 2.2.3 on 2019-07-31 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0022_auto_20190728_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='has_mined',
            field=models.BooleanField(default=False),
        ),
    ]