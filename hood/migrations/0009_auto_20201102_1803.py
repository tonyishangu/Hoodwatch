# Generated by Django 3.0.2 on 2020-11-02 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0008_auto_20201102_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='hood.NeighbourHood'),
        ),
        migrations.AlterField(
            model_name='post',
            name='hood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood_post', to='hood.NeighbourHood'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='hood.NeighbourHood'),
        ),
    ]
