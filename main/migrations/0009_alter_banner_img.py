# Generated by Django 4.0.4 on 2022-07-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_banner_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(upload_to='banner_imgs/'),
        ),
    ]
