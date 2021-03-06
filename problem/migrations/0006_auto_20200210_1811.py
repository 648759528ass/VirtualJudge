# Generated by Django 3.0.3 on 2020-02-10 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0002_language'),
        ('problem', '0005_auto_20200208_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='destination.Platform'),
        ),
        migrations.AlterField(
            model_name='request',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='problem.Problem'),
        ),
    ]
