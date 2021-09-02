# Generated by Django 3.1.4 on 2021-08-06 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_dairycatagory'),
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='catagory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.dairycatagory'),
            preserve_default=False,
        ),
    ]