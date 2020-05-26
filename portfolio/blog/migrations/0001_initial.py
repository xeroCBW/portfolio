# Generated by Django 2.0.2 on 2020-05-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='文章标题', max_length=100)),
                ('create_date', models.DateField()),
                ('pic', models.ImageField(default='default.png', upload_to='images/')),
                ('text', models.TextField(default='文章正文')),
            ],
        ),
    ]