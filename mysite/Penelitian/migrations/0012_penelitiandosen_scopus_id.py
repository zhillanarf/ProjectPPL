# Generated by Django 5.1.1 on 2024-11-07 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Penelitian', '0011_remove_penelitiandosen_scopus_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='penelitiandosen',
            name='scopus_id',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
