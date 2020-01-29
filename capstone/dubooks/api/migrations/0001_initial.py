# Generated by Django 3.0.2 on 2020-01-28 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traditional', models.CharField(max_length=30)),
                ('simplified', models.CharField(max_length=30)),
                ('english', models.CharField(max_length=200)),
                ('pinyin', models.CharField(max_length=50)),
                ('hsk', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True)),
                ('lists', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.List')),
                ('words', models.ManyToManyField(to='api.Word')),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='words',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Word'),
        ),
    ]
