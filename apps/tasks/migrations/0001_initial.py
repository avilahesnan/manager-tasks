# Generated by Django 4.2.7 on 2024-01-29 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('PROGRAMMING', 'programming'), ('COMPUTER SCIENCE', 'computer science'), ('MATHEMATICS', 'mathematics'), ('PORTUGUESE', 'portuguese'), ('ENGLISH', 'english'), ('LEGISLATION', 'legislation')], default='NOT SPECIFIED', max_length=100)),
                ('subject', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('term', models.DateField()),
                ('is_completed', models.BooleanField(default=False)),
                ('cover', models.ImageField(blank=True, upload_to='tasks/covers/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
