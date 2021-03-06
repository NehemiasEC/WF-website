# Generated by Django 2.2.4 on 2019-10-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_shipping_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='purchaser_email',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_country',
            new_name='recipient_address_country',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_locality',
            new_name='recipient_address_locality',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_region',
            new_name='recipient_address_region',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='family_name',
            new_name='recipient_family_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='given_name',
            new_name='recipient_given_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='po_box_number',
            new_name='recipient_po_box_number',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='postal_code',
            new_name='recipient_postal_code',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_address',
            new_name='recipient_street_address',
        ),
        migrations.AddField(
            model_name='order',
            name='purchaser_family_name',
            field=models.CharField(blank=True, default='', help_text='Enter the family name for the recipient.', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='purchaser_given_name',
            field=models.CharField(default='', help_text='Enter the given name for the recipient.', max_length=255),
        ),
    ]
