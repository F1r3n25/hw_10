# Generated by Django 4.2.7 on 2023-12-01 12:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0002_author_tag_quote_created_at_alter_quote_quote_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="born_location",
            field=models.CharField(max_length=100),
        ),
    ]
