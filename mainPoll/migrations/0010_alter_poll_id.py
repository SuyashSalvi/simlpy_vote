# Generated by Django 4.1.3 on 2023-06-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPoll', '0009_alter_poll_id_alter_pollchoices_poll_rs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='id',
            field=models.CharField(default='14937837', editable=False,
                                   max_length=50, primary_key=True, serialize=False),
        ),
    ]
