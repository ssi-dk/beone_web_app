# Generated by Django 4.1.2 on 2023-06-26 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparisons', '0051_remove_comparison_distance_matrix_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comparison',
            name='status',
        ),
        migrations.RemoveField(
            model_name='comparison',
            name='tree_average',
        ),
        migrations.RemoveField(
            model_name='comparison',
            name='tree_complete',
        ),
        migrations.RemoveField(
            model_name='comparison',
            name='tree_single',
        ),
        migrations.AddField(
            model_name='comparison',
            name='dm_status',
            field=models.CharField(choices=[('NODATA', 'No data'), ('REQUESTED', 'Requested'), ('VALID', 'Valid'), ('ERROR', 'Request was unsuccesful'), ('OBSOLETE', 'No longer valid')], default='NODATA', max_length=15),
        ),
    ]
