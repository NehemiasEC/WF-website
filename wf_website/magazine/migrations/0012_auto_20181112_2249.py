# Generated by Django 2.1.3 on 2018-11-12 22:49

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0011_auto_20181112_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazineissuefeaturedarticle',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='magazine.MagazineArticle'),
        ),
        migrations.AlterField(
            model_name='magazineissuefeaturedarticle',
            name='issue',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_articles', to='magazine.MagazineIssue'),
        ),
    ]