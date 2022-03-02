# Generated by Django 4.0.3 on 2022-03-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstance',
            old_name='inprint',
            new_name='imprint',
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='select a genre for this book', to='catalog.genre'),
        ),
    ]