# Generated by Django 3.1.4 on 2021-07-27 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistcatagory',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='TodoListItem',
        ),
    ]
