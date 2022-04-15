# Generated by Django 4.0 on 2022-04-15 13:01

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('raw_file', models.FileField(upload_to='files/podcasts')),
                ('cover_image', models.ImageField(upload_to='media/podcast_cover_images')),
                ('name', models.CharField(max_length=128)),
                ('contributors', models.TextField(help_text='All contributors comma or new line seperated here')),
                ('subject', models.CharField(max_length=32)),
                ('length', models.DurationField()),
                ('publishing_date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
