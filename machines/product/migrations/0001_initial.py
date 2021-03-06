# Generated by Django 2.2.5 on 2019-09-07 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=512, null=True)),
                ('image', models.ImageField(upload_to='core/picture/image')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=128)),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('on_sale', models.BooleanField(db_index=True, default=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='product.Module')),
                ('pictures', models.ManyToManyField(blank=True, null=True, related_name='variations', to='product.Picture')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='picture_primary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Picture'),
        ),
        migrations.AddField(
            model_name='module',
            name='pictures',
            field=models.ManyToManyField(blank=True, null=True, related_name='modules', to='product.Picture'),
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('on_sale', models.BooleanField(db_index=True, default=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('picture_primary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='machines', to='product.Picture')),
                ('pictures', models.ManyToManyField(to='product.Picture')),
                ('variations', models.ManyToManyField(blank=True, related_name='machines', to='product.Variation')),
            ],
        ),
    ]
