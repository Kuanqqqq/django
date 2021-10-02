# Generated by Django 3.2.7 on 2021-10-01 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manufacturer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturer.brand')),
            ],
        ),
    ]