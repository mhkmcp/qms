# Generated by Django 3.1.7 on 2021-04-01 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0012_auto_20210331_2323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('id',), 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ('created_at',), 'verbose_name': 'Quiz', 'verbose_name_plural': 'Quizzes'},
        ),
        migrations.AlterModelOptions(
            name='text',
            options={'ordering': ('created_at',), 'verbose_name': 'Text', 'verbose_name_plural': 'Texts'},
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='choice_option',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='text',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='choice',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='quiz.question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='text',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='text',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='quiz.question'),
        ),
        migrations.DeleteModel(
            name='Radio',
        ),
    ]
