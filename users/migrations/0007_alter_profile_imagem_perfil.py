# Generated by Django 4.0.4 on 2022-05-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_contato_profile_contato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='imagem_perfil',
            field=models.ImageField(blank=True, default='usuario.png', null=True, upload_to='users/'),
        ),
    ]