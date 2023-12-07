# Generated by Django 4.2.7 on 2023-12-06 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SharedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=4, unique=True)),
                ('file', models.FileField(upload_to='shared_files/')),
            ],
        ),
    ]