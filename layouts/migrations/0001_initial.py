# Generated by Django 4.0.4 on 2022-05-11 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComanyProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_id', models.IntegerField(default=0)),
                ('product_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_id', models.IntegerField(default=0)),
                ('company_name', models.CharField(default=None, max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPlanogram',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_id', models.IntegerField(default=0)),
                ('planogram_id', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Planogram',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('planogram_id', models.IntegerField(default=0)),
                ('planogram_name', models.CharField(default=None, max_length=255)),
                ('planogram_photo', models.CharField(default=None, max_length=255)),
                ('order', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanogramProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.IntegerField(default=0)),
                ('planogram_id', models.IntegerField(default=0)),
                ('rows', models.IntegerField(default=0)),
                ('order', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('store_image_id', models.IntegerField(default=0)),
                ('result', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.CharField(default=None, max_length=255)),
                ('product_name', models.CharField(default=None, max_length=255)),
                ('product_photo', models.CharField(default=None, max_length=255)),
                ('order', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResultImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('result_id', models.IntegerField(default=0)),
                ('result_image_name', models.CharField(default=None, max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StoreImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
                ('photo_name', models.CharField(default=None, max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
