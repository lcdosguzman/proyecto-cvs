# Generated by Django 5.0.1 on 2024-02-13 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCurriculum', '0007_alter_educacion_periodo_fin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aptitud', models.CharField(max_length=50)),
            ],
        ),
    ]