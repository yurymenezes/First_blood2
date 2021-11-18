# Generated by Django 3.2.9 on 2021-11-11 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_comentarios', '0002_alter_comentario_nome_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(verbose_name='Comentário'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='email_comentario',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='nome_comentario',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='usuario_comentario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
