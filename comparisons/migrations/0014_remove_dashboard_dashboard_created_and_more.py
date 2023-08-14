# Generated by Django 4.1.9 on 2023-08-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparisons', '0013_alter_comparison_options_alter_dashboard_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='dashboard_created',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='uuid',
        ),
        migrations.AddField(
            model_name='dashboard',
            name='id',
            field=models.CharField(default=1, editable=False, max_length=22, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
