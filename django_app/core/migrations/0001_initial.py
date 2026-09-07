# Generated manually for the HA demo

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('author', models.CharField(blank=True, default='Anonymous', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_on_host', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
