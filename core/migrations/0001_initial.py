# Generated by Django 5.0 on 2025-07-17 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default='Write Something')),
                ('price1', models.IntegerField(default=0)),
                ('price2', models.IntegerField(default=0)),
                ('price3', models.IntegerField(default=0)),
                ('price4', models.IntegerField(default=0)),
                ('price5', models.IntegerField(default=0)),
                ('cover_img', models.ImageField(default='image', upload_to='img/post_cover')),
                ('img1', models.ImageField(default='img/post_cover/image_1.jpg', upload_to='img/img')),
                ('img2', models.ImageField(default='img/post_cover/image_1.jpg', upload_to='img/img')),
                ('img3', models.ImageField(default='img/post_cover/image_1.jpg', upload_to='img/img')),
                ('img4', models.ImageField(default='img/post_cover/image_1.jpg', upload_to='img/img')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='product', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('service', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='packages', to='core.service')),
            ],
        ),
    ]
