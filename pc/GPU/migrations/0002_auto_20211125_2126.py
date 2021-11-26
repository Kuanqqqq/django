# Generated by Django 3.2.7 on 2021-11-26 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specifics', '0001_initial'),
        ('GPU', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chipset',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='specifics.color'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='memory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='specifics.memory'),
        ),
    ]