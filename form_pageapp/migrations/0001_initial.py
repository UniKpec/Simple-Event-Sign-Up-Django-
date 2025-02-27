# Generated by Django 5.1.3 on 2025-02-05 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
    ]
