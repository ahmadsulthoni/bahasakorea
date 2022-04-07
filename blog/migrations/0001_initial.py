# Generated by Django 4.0.3 on 2022-04-03 08:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_comment', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField()),
                ('memes_photo', models.ImageField(upload_to='')),
                ('upload', models.DateTimeField(auto_now_add=True)),
                ('comments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                               to='blog.comment')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.photos'),
        ),
        migrations.AddField(
            model_name='comment',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
