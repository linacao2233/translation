# Generated by Django 2.0 on 2017-12-14 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chinese', models.TextField(blank=True, null=True)),
                ('English', models.TextField(blank=True, null=True)),
                ('googletranslate', models.TextField(blank=True, null=True)),
                ('order', models.FloatField(default=1.0)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Chapter')),
            ],
        ),
    ]
