# Generated by Django 3.2.7 on 2021-09-28 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_repository_app', '0003_auto_20210927_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='creator',
            field=models.CharField(default='Unkown', max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(default='Unkown', max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]