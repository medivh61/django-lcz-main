# Generated by Django 4.0.4 on 2022-05-09 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_quiz_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='topic',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]