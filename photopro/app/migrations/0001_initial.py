# Generated by Django 3.2.17 on 2023-02-02 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='myimabe')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
