# Generated by Django 5.0.3 on 2024-03-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_delete_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='category',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='update',
        ),
        migrations.AddField(
            model_name='blogs',
            name='description',
            field=models.CharField(default=1, max_length=255, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]