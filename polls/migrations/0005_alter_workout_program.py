# Generated by Django 4.2.1 on 2023-06-01 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_exercise_id_alter_program_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.program'),
        ),
    ]