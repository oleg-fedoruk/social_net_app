# Generated by Django 4.1.3 on 2023-01-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='header',
            field=models.TextField(blank=True, null=True, verbose_name='Заголовок'),
        ),
    ]
