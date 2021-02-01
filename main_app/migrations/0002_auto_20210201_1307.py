# Generated by Django 3.1.3 on 2021-02-01 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='clothing',
            name='color',
            field=models.ForeignKey(choices=[('Pink', 'Pink'), ('Red', 'Red'), ('Orange', 'Orange'), ('Beige', 'Beige'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Light Blue', 'Light Blue'), ('Dark Blue', 'Dark Blue'), ('Purple', 'Purple'), ('Brown', 'Brown'), ('Grey', 'Grey')], default='Pink', max_length=10, on_delete=django.db.models.deletion.CASCADE, to='main_app.color'),
        ),
    ]
