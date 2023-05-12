# Generated by Django 4.1.2 on 2023-05-12 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comparisons', '0034_remove_cluster_species'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='species',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='comparisons.species'),
            preserve_default=False,
        ),
    ]
