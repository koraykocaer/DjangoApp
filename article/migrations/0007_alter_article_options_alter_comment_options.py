# Generated by Django 5.0.2 on 2024-02-22 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]