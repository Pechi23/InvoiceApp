# Generated by Django 5.0 on 2024-01-09 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0003_alter_invoice_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="number",
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
