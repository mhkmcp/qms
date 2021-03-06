# Generated by Django 3.1.7 on 2021-03-31 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20210330_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radio',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='radio_related', to='quiz.question', verbose_name='question '),
        ),
        migrations.AlterField(
            model_name='text',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='text_related', to='quiz.question', verbose_name='question '),
        ),
    ]
