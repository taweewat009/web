# Generated by Django 3.2.8 on 2021-10-25 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20211025_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbook',
            name='message',
            field=models.CharField(max_length=200),
        ),
    ]