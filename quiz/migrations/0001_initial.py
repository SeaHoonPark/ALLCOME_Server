# Generated by Django 2.2.1 on 2019-05-18 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('pr_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('subject', models.CharField(max_length=50)),
                ('image', models.URLField()),
                ('title', models.TextField()),
                ('answer', models.IntegerField()),
                ('explain', models.TextField()),
                ('choice_1', models.CharField(max_length=50)),
                ('choice_2', models.CharField(max_length=50)),
                ('choice_3', models.CharField(max_length=50)),
                ('choice_4', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('subject',),
            },
        ),
    ]
