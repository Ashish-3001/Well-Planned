# Generated by Django 3.1.4 on 2021-08-03 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20210727_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='DairyCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
