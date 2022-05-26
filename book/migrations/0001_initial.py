# Generated by Django 4.0.4 on 2022-05-25 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128)),
                ('description', models.TextField(blank=True)),
                ('count', models.IntegerField(default=10)),
                ('authors', models.ManyToManyField(related_name='books', to='author.author')),
            ],
        ),
    ]
