# Generated by Django 4.2.1 on 2023-07-12 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_transaccion_id_remove_transaccion_target_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
        migrations.RemoveField(
            model_name='task',
            name='datacompleted',
        ),
        migrations.RemoveField(
            model_name='task',
            name='important',
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='usuario_destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarioDestinatario', to='tasks.usuario'),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='usuario_origen',
            field=models.CharField(max_length=64),
        ),
    ]
