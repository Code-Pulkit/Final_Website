# Generated by Django 4.0.6 on 2022-07-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposium', '0010_alter_model_all_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='text',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='point',
            name='label',
            field=models.IntegerField(),
        ),
    ]
