# Generated by Django 5.1.6 on 2025-02-22 19:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0002_alter_vote_unique_together_remove_vote_crime_post_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crimepost',
            name='upvote_count',
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_type', models.SmallIntegerField(choices=[(1, 'Upvote'), (-1, 'Downvote')])),
                ('crime_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='crime.crimepost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'crime_post')},
            },
        ),
    ]
