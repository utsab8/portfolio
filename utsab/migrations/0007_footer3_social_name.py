# Generated by Django 4.1.5 on 2023-01-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utsab', '0006_footer1_footer2_footer3_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer3',
            name='social_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
