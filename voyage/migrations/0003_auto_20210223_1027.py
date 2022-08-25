# Generated by Django 3.1.5 on 2021-02-23 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0002_auto_20210223_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='voyage',
        ),
        migrations.AddField(
            model_name='voyage',
            name='destination',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='voyage.destination'),
            preserve_default=False,
        ),
    ]
