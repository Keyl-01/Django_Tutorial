# Generated by Django 3.1.14 on 2022-08-08 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial_django', '0003_auto_20220803_0900'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={},
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default=None, upload_to='courses/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', related_query_name='lessons_query', to='tutorial_django.course'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(default=None, upload_to='courses/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='lessons', to='tutorial_django.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together=set(),
        ),
    ]
