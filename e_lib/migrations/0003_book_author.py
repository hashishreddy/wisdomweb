# Generated by Django 4.2.4 on 2023-08-23 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_lib', '0002_delete_myuser_delete_teacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=120, null=True, verbose_name='author'),
        ),
    ]
