# Generated by Django 2.1.7 on 2019-02-20 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0019_auto_20190216_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magazinearticle',
            name='department',
        ),
        migrations.DeleteModel(
            name='MagazineDepartment',
        ),
    ]