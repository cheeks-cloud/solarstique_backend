# Generated by Django 4.2.1 on 2023-05-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(default='https://drive.google.com/file/d/1he_HC1GDW_Xw4ekPXAf4H_A8W6wl9uMd/view?usp=share_link'),
        ),
    ]
