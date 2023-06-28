# Generated by Django 4.1.2 on 2023-06-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparisons', '0053_comparison_always_calculate_dm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comparison',
            name='dm_status',
            field=models.CharField(choices=[('NODATA', 'No data'), ('PENDING', 'Pending'), ('VALID', 'Valid'), ('ERROR', 'Request was unsuccesful'), ('OBSOLETE', 'Obsolete')], default='NODATA', max_length=15),
        ),
    ]
