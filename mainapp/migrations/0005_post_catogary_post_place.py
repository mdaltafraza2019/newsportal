# Generated by Django 4.1.5 on 2023-01-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='catogary',
            field=models.CharField(blank=True, choices=[('crime', 'crime'), ('education', 'education'), ('sports', 'sports'), ('entertenment', 'entertenment'), ('golbal', 'golbal')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='place',
            field=models.CharField(blank=True, choices=[('purnia', 'purnia'), ('katihar', 'katihar'), ('america', 'america'), ('delhi', 'delhi'), ('mumbai', 'mumbai')], max_length=100, null=True),
        ),
    ]
