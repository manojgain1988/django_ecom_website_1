# Generated by Django 5.0.4 on 2024-04-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0004_alter_slider_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={},
        ),
        migrations.RenameField(
            model_name='slider',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='image',
        ),
        migrations.AddField(
            model_name='slider',
            name='banner',
            field=models.ImageField(default=1, upload_to='banners'),
            preserve_default=False,
        ),
    ]
