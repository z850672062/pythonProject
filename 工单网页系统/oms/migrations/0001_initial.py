# Generated by Django 3.2.4 on 2021-06-19 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('operator_id', models.AutoField(primary_key=True, serialize=False)),
                ('operator_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500)),
                ('result', models.CharField(max_length=200)),
                ('status', models.IntegerField(choices=[(0, '未处理'), (1, '已完成')], default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.customer')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.operator')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oms.question')),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
    ]
