# Generated by Django 4.1.5 on 2023-01-20 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_ad_slug_alter_ad_description_alter_ad_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.categories'),
        ),
    ]
