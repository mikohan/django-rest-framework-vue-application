# Generated by Django 3.0.2 on 2020-02-07 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programmers', '0003_programmer_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='paradigm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lang', to='programmers.Paradigm'),
        ),
    ]