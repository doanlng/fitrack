# Generated by Django 4.2.1 on 2023-05-31 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_workout_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='program',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]