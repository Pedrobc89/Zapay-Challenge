# Generated by Django 2.2.1 on 2019-05-06 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('got', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=10)),
                ('img', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]