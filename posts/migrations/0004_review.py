# Generated by Django 5.0.6 on 2024-07-18 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=100)),
                ('ratings', models.IntegerField()),
                ('feedback', models.CharField(max_length=200)),
            ],
        ),
    ]
