# Generated by Django 2.2 on 2019-04-15 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapic', '0006_auto_20190415_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='email',
            field=models.CharField(max_length=20, null=True),
        ),
    ]