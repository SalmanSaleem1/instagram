# Generated by Django 2.2 on 2019-04-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instapic', '0003_photo_phototag'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.IntegerField()),
                ('liker', models.CharField(max_length=20)),
            ],
        ),
    ]
