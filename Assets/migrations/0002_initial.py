# Generated by Django 4.1.3 on 2022-11-12 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company', '0001_initial'),
        ('Assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetassign',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.employee'),
        ),
    ]
