# Generated by Django 2.2.17 on 2021-01-07 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interactwel', '0025_auto_20210107_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteractwelProjectJoinRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=256)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interactwel.InteractwelProject')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interactwel.InteractwelUser')),
            ],
            options={
                'verbose_name': 'Interactwel Project Join Request',
                'verbose_name_plural': 'Interactwel Project Join Request',
                'db_table': 'interactwel_project_join_request',
                'managed': True,
                'unique_together': {('project_id', 'user_id')},
            },
        ),
    ]
