# Generated by Django 2.2.3 on 2019-07-28 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0021_auto_20190726_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='can_mine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='has_rename',
            field=models.BooleanField(default=False),
        ),
    ]
