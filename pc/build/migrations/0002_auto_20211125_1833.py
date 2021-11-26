# Generated by Django 3.2.7 on 2021-11-26 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CPU', '0004_alter_cpu_image'),
        ('GPU', '0001_initial'),
        ('build', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='cpu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CPU.cpu'),
        ),
        migrations.AlterField(
            model_name='build',
            name='gpu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPU.gpu'),
        ),
        migrations.AlterField(
            model_name='build',
            name='user_token',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
