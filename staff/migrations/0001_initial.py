# Generated by Django 4.0 on 2022-06-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('position', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to='staff_images')),
                ('present_in_landing_page', models.BooleanField(default=False)),
            ],
        ),
    ]
