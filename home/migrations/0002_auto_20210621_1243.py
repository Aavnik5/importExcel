# Generated by Django 3.1.3 on 2021-06-21 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='handleexcel',
            old_name='excel_file',
            new_name='excelfile',
        ),
    ]