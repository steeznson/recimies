# Generated by Django 2.1.3 on 2018-11-11 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import social.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='../static//img/default-image.jpg', upload_to=social.models._recipie_image_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]