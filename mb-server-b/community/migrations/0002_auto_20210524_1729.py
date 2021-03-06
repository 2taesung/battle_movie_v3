# Generated by Django 3.2.3 on 2021-05-24 08:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='vote_users',
        ),
        migrations.AddField(
            model_name='movie',
            name='vote_users',
            field=models.ManyToManyField(related_name='vote_movies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='community',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
