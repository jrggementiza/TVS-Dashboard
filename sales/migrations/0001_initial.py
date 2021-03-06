# Generated by Django 2.1.5 on 2019-03-14 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(choices=[('SHP', 'Shopee'), ('FB', 'Facebook'), ('IG', 'Instagram'), ('CRL', 'Carousel'), ('GRP', 'GROUPS')], max_length=3)),
                ('payment_method', models.CharField(choices=[('SHP', 'Shopee'), ('BDO', 'BDO'), ('BPI', 'BPI')], max_length=3)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item')),
            ],
        ),
    ]
