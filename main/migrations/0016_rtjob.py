# Generated by Django 4.0.7 on 2022-09-01 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0015_remove_dataset_mongo_ids'),
    ]

    operations = [
        migrations.CreateModel(
            name='RTJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('INITIALIZING', 'Initializing'), ('READY', 'Ready'), ('RUNNING', 'Running'), ('SUCCEEDED', 'Succeeded'), ('FAILED', 'Failed'), ('INVALID', 'Invalid')], default='INITIALIZING', max_length=12)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.dataset')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
