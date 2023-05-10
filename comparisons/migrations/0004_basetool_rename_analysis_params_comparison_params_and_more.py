# Generated by Django 4.2.1 on 2023-05-10 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comparisons', '0003_analysistool_remove_comparison_analysis_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('cgmlst', 'cgMLST'), ('snp', 'SNP')], default='cgmlst', max_length=8)),
                ('name', models.CharField(max_length=20)),
                ('version', models.CharField(max_length=8)),
            ],
        ),
        migrations.RenameField(
            model_name='comparison',
            old_name='analysis_params',
            new_name='params',
        ),
        migrations.RemoveField(
            model_name='comparison',
            name='analysis_subtype',
        ),
        migrations.RemoveField(
            model_name='comparison',
            name='tool',
        ),
        migrations.AddField(
            model_name='comparison',
            name='linkage_method',
            field=models.CharField(choices=[('SINGLE', 'Single'), ('COMPLETE', 'Complete'), ('UPGMA', 'UPGMA'), ('NJ', 'Neighbor Joining')], default='SINGLE', max_length=10),
        ),
        migrations.DeleteModel(
            name='AnalysisTool',
        ),
        migrations.AddConstraint(
            model_name='basetool',
            constraint=models.UniqueConstraint(fields=('name', 'version'), name='tool_name_version_unique'),
        ),
        migrations.AddField(
            model_name='comparison',
            name='base_tool',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='comparisons.basetool'),
        ),
    ]
