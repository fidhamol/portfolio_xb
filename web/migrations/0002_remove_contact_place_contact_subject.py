# Generated by Django 4.2.5 on 2023-09-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='place',
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(choices=[('', 'Subject'), ('Digital Marketing', 'Digital Marketing'), ('Web Design', 'Web Design')], default=1, max_length=120),
            preserve_default=False,
        ),
    ]
