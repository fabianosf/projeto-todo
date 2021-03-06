# Generated by Django 2.1.5 on 2022-02-28 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descricao',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='titulo',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.CharField(choices=[('doing', 'Doing'), ('done', 'Done')], max_length=5),
        ),
    ]
