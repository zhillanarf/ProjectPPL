# Generated by Django 5.1.1 on 2024-11-15 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Penelitian', '0015_alter_penelitiandosen_abstract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='penelitiandosen',
            name='topikpenelitian_id',
        ),
        migrations.AddField(
            model_name='penelitiandosen',
            name='topik_penelitian_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topik_penelitian_1', to='Penelitian.topikpenelitian'),
        ),
        migrations.AddField(
            model_name='penelitiandosen',
            name='topik_penelitian_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topik_penelitian_2', to='Penelitian.topikpenelitian'),
        ),
        migrations.AddField(
            model_name='penelitiandosen',
            name='topik_penelitian_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topik_penelitian_3', to='Penelitian.topikpenelitian'),
        ),
    ]
