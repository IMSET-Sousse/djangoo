# Generated by Django 5.1.6 on 2025-03-21 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='categorie',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='date_peremption',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='prix',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='quantite_stock',
        ),
        migrations.AlterField(
            model_name='produit',
            name='nom',
            field=models.CharField(max_length=100),
        ),
    ]
