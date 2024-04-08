# Generated by Django 5.0.3 on 2024-03-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_delete_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='android',
            name='type_dev',
            field=models.CharField(default=1, max_length=255, verbose_name='Тип разработки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='backend',
            name='type_dev',
            field=models.CharField(default=1, max_length=255, verbose_name='Тип разработки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desinger',
            name='type_dev',
            field=models.CharField(default=1, max_length=255, verbose_name='Тип разработки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='frontend',
            name='type_dev',
            field=models.CharField(default=1, max_length=255, verbose_name='Тип разработки'),
            preserve_default=False,
        ),
    ]