# Generated by Django 4.0.5 on 2022-07-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]