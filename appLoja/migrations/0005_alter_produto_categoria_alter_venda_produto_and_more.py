# Generated by Django 5.1.1 on 2024-09-25 22:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLoja', '0004_alter_produto_unidade'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appLoja.categoria'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appLoja.produto'),
        ),
        migrations.AlterField(
            model_name='venda',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
