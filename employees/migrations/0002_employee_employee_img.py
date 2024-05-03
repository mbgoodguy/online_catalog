# Generated by Django 5.0.4 on 2024-05-03 09:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="employee_img",
            field=models.ImageField(
                blank=True,
                help_text="96x96px",
                upload_to="images/%Y/%m/%d",
                verbose_name="employee_photo",
            ),
        ),
    ]
