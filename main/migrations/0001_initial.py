# Generated by Django 3.2.16 on 2022-12-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssurancePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=10000)),
                ('bannier', models.ImageField(upload_to='bannier/')),
            ],
        ),
    ]
