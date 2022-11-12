# Generated by Django 4.1.3 on 2022-11-12 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('asset_id', models.IntegerField(primary_key=True, serialize=False)),
                ('asset_name', models.CharField(max_length=30)),
                ('asset_type', models.CharField(max_length=30)),
                ('asset_price', models.IntegerField()),
                ('asset_purchase_date', models.DateField()),
                ('asset_warranty', models.IntegerField()),
                ('asset_status', models.CharField(max_length=30)),
                ('asset_location', models.CharField(max_length=30)),
                ('asset_description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employess',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_email', models.EmailField(max_length=30)),
                ('emp_address', models.CharField(max_length=30)),
                ('emp_salary', models.IntegerField()),
                ('emp_dob', models.DateField()),
                ('Phone', models.DecimalField(decimal_places=0, max_digits=11, verbose_name='Phone Number')),
                ('Joinnig_date', models.DateField(max_length=50, verbose_name='Joining Date')),
                ('username', models.CharField(max_length=30)),
                ('emp_name', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssetAssign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_assign_date', models.DateField()),
                ('asset_return_date', models.DateField()),
                ('asset_assign_status', models.CharField(max_length=30)),
                ('asset_log', models.CharField(max_length=30)),
                ('asset_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assets.assets')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assets.employess')),
            ],
        ),
    ]