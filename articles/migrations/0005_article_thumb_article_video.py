# Generated by Django 4.1 on 2022-08-29 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='1.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.FileField(blank=True, default='1.mp4', upload_to='video%y'),
        ),
    ]
