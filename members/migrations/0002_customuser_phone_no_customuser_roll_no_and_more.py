# Generated by Django 4.2.4 on 2023-08-23 13:53

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='Phone No.'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='roll_no',
            field=models.IntegerField(null=True, verbose_name='roll no.'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('', 'select'), ('teacher', 'Teacher'), ('student', 'Student')], default='student', max_length=20, null=True),
        ),
    ]
