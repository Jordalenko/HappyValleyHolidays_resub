# Generated by Django 4.2.21 on 2025-06-07 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cottages', '0011_cottage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cottage',
            name='image',
        ),
        migrations.CreateModel(
            name='CottageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cottages/')),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('cottage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='cottages.cottage')),
            ],
        ),
    ]
