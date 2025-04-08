from django.db import migrations
from djongo import models
from django.contrib.auth.models import User

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('_id', models.ObjectIdField(primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('members', models.ArrayReferenceField(on_delete=models.CASCADE, to=User)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('_id', models.ObjectIdField(primary_key=True)),
                ('activity_type', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=models.CASCADE, to=User)),
            ],
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('_id', models.ObjectIdField(primary_key=True)),
                ('score', models.IntegerField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=models.CASCADE, to=User)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('_id', models.ObjectIdField(primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.DurationField()),
                ('difficulty', models.CharField(max_length=20)),
            ],
        ),
    ]
