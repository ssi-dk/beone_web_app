# Generated by Django 4.1.9 on 2023-08-14 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparisons', '0015_alter_dashboard_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='id',
            field=models.CharField(editable=False, max_length=22, primary_key=True, serialize=False),
        ),
    ]
