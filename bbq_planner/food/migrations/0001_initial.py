# Generated by Django 2.0.2 on 2018-02-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(default='meat', max_length=200)),
                ('food_type', models.CharField(default='beef', max_length=200)),
            ],
            options={
                'db_table': 'food',
            },
        ),
    ]