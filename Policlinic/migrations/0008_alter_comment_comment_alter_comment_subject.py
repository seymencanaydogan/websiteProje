# Generated by Django 4.1.2 on 2022-12-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Policlinic', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
