# Generated by Django 2.2.2 on 2019-07-01 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(default=None, on_delete='CASCADE', to='MainApp.Category'),
        ),
    ]
