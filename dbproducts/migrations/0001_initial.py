# Generated by Django 3.0 on 2019-12-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=150)),
                ('nutri_grade', models.IntegerField()),
                ('web_link', models.URLField()),
                ('categories', models.ManyToManyField(to='dbproducts.Category')),
            ],
        ),
    ]
