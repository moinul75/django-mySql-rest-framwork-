# Generated by Django 4.1.7 on 2023-02-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=400)),
                ('Category', models.CharField(max_length=400)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Description', models.TextField()),
                ('Stars', models.IntegerField()),
            ],
        ),
    ]
