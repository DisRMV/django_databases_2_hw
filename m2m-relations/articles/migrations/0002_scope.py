# Generated by Django 3.1.2 on 2021-12-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Тэг')),
                ('articles', models.ManyToManyField(related_name='scopes', to='articles.Article')),
            ],
        ),
    ]