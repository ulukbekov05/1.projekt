# Generated by Django 5.1.4 on 2024-12-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_KY',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_KY',
            field=models.CharField(max_length=65, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_en',
            field=models.CharField(max_length=65, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_ru',
            field=models.CharField(max_length=65, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='have',
            field=models.BooleanField(default=True, verbose_name='в наличи'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена'),
        ),
    ]
