# Generated by Django 5.0.6 on 2024-07-18 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas_sharingann', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='descripcion',
            field=models.TextField(),
        ),
    ]