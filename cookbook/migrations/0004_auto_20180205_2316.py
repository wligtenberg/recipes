# Generated by Django 2.0.2 on 2018-02-05 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0003_recipe_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='link',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='cookbook.Keyword'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='path',
            field=models.CharField(default='', max_length=512),
        ),
    ]
