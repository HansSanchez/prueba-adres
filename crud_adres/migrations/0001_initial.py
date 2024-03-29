# Generated by Django 5.0.1 on 2024-01-28 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acquisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.BigIntegerField(default=0)),
                ('administrative_unit', models.CharField(max_length=255)),
                ('type_of_goods_or_services', models.CharField(max_length=255)),
                ('quantity', models.BigIntegerField(default=0)),
                ('unit_value', models.BigIntegerField(default=0)),
                ('total_value', models.CharField(max_length=255)),
                ('acquisition_date', models.CharField(max_length=255)),
                ('supplier', models.CharField(max_length=255)),
                ('documentation', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('disabled_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'acquisitions',
            },
        ),
    ]
