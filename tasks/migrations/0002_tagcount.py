# Generated by Django 2.2.4 on 2019-08-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_slug', models.CharField(max_length=128)),
                ('tag_name', models.CharField(max_length=128)),
                ('tag_id', models.PositiveIntegerField(default=0)),
                ('tag_count', models.PositiveIntegerField(db_index=True, default=0)),
            ],
        ),
    ]
