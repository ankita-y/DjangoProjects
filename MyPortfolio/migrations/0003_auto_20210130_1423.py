# Generated by Django 3.1.3 on 2021-01-30 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyPortfolio', '0002_auto_20210130_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='art_images',
            field=models.ImageField(blank=True, null=True, upload_to='shop/pics'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='img_desc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='projects',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='skillper',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='skills',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='thoughts',
            field=models.TextField(blank=True, null=True),
        ),
    ]
