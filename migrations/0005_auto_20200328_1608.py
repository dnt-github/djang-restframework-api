# Generated by Django 3.0.4 on 2020-03-28 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200328_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='data_sheet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.DataSheet'),
        ),
    ]