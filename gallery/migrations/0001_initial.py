# Generated by Django 4.0 on 2022-06-02 20:20

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', models.ImageField(upload_to='gallery_photos')),
                ('caption', models.CharField(max_length=256)),
                ('attenders', models.TextField(blank=True, help_text='All attenders comma or new line seperated here', null=True)),
                ('photographer', models.CharField(max_length=64)),
                ('shooting_date', models.DateField()),
                ('publishing_date', models.DateField()),
                ('views', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
