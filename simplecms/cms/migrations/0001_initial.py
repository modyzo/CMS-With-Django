# Generated by Django 3.0 on 2020-05-05 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='hey', max_length=50)),
                ('username', models.CharField(default='modyzo', max_length=50)),
                ('age', models.IntegerField(blank=True, default=0)),
                ('email', models.EmailField(default='info@modyzo.com', max_length=254)),
            ],
        ),
    ]
