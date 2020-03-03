# Generated by Django 2.0.6 on 2020-03-03 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACharge',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('gold', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'a_charge',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CArticle',
            fields=[
                ('date', models.DateField(auto_created=True, auto_now=True, max_length=50)),
                ('a_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=5, null=True)),
                ('isfree', models.TextField(blank=True, null=True)),
                ('fabulous', models.IntegerField(blank=True, null=True)),
                ('profit', models.FloatField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('state', models.IntegerField(choices=[(0, '审核中'), (1, '已通过'), (2, '未通过')], default=0)),
                ('note', models.TextField(default='')),
            ],
            options={
                'db_table': 'c_article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CArticleTag',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'c_article_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CATag',
            fields=[
                ('a_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('t_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'c_a_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CImages',
            fields=[
                ('i_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('i_name', models.CharField(blank=True, max_length=50, null=True)),
                ('images', models.TextField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'c_images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CMTag',
            fields=[
                ('m_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('t_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'c_m_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CMusic',
            fields=[
                ('m_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('m_name', models.CharField(blank=True, max_length=60, null=True)),
                ('lyrics', models.CharField(blank=True, max_length=50, null=True)),
                ('composition', models.CharField(blank=True, max_length=50, null=True)),
                ('music', models.TextField(blank=True, null=True)),
                ('isfree', models.TextField()),
            ],
            options={
                'db_table': 'c_music',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CMusicTag',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'c_music_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('time', models.CharField(blank=True, max_length=20, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FirstImages',
            fields=[
                ('img_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'first_images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FirstSentence',
            fields=[
                ('s_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sentence', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'first_sentence',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MAbility',
            fields=[
                ('m_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('m_user', models.CharField(blank=True, max_length=50, null=True)),
                ('m_concent', models.TextField(blank=True, null=True)),
                ('m_notice', models.TextField(blank=True, null=True)),
                ('m_advertisement', models.TextField(blank=True, null=True)),
                ('m_msg', models.TextField(blank=True, null=True)),
                ('m_illegal_user', models.CharField(blank=True, max_length=20, null=True)),
                ('m_illegal_content', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'm_ability',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('m_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('m_account', models.CharField(blank=True, max_length=30, null=True)),
                ('m_pwd', models.CharField(blank=True, max_length=50, null=True)),
                ('m_email', models.CharField(blank=True, db_column='m_Email', max_length=40, null=True)),
                ('m_telephone', models.CharField(blank=True, max_length=30, null=True)),
                ('m_set', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'manager',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MCharge2',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('gold', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'm_charge2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TAdminLevel',
            fields=[
                ('id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('lev', models.IntegerField()),
                ('category', models.CharField(max_length=20)),
                ('indetail', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_admin_level',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TAdvertising',
            fields=[
                ('a_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.CharField(max_length=100)),
                ('state', models.IntegerField(choices=[(0, '审核中'), (1, '已通过'), (2, '未通过')], default=0)),
            ],
            options={
                'db_table': 't_advertising',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TBuyVip',
            fields=[
                ('id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('open_time', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 't_buy_vip',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='THaveread',
            fields=[
                ('have_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('read_time', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 't_haveread',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TLevelSuffer',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=70, primary_key=True, serialize=False)),
                ('grade', models.IntegerField()),
                ('experience', models.IntegerField()),
            ],
            options={
                'db_table': 't_level_suffer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TMessageFeedback',
            fields=[
                ('id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('qq', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 't_message_feedback',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TSlidesshow',
            fields=[
                ('img_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('image', models.TextField()),
                ('link', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 't_slidesshow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TSysRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True, unique=True)),
            ],
            options={
                'db_table': 't_sys_role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TSysUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('auth_string', models.CharField(max_length=32)),
                ('nick_name', models.CharField(blank=True, max_length=20, null=True)),
                ('role_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_sys_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TTask',
            fields=[
                ('task_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('reward', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('task_type', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 't_task',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TUsermessage',
            fields=[
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=16, null=True)),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 't_usermessage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TUserTasks',
            fields=[
                ('t_u_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('isfinish', models.IntegerField(blank=True, null=True)),
                ('finish_time', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 't_user_tasks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TVipClassify',
            fields=[
                ('v_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('days', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('dis_days', models.IntegerField(blank=True, null=True)),
                ('whether', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_vip_classify',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UCollection',
            fields=[
                ('collection_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('datetime', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'u_collection',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UDownload',
            fields=[
                ('d_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'u_download',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UFabulous',
            fields=[
                ('datatime', models.CharField(max_length=20)),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'u_fabulous',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UGiveReward',
            fields=[
                ('u_g_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('reward', models.CharField(blank=True, max_length=70, null=True)),
                ('time', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'u_give_reward',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UPayClassify',
            fields=[
                ('pc_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('rmb', models.IntegerField(db_column='RMB')),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'u_pay_classify',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UPayrank',
            fields=[
                ('p_r_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('time', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'u_payrank',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
                ('vip_datetime', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.CharField(max_length=100)),
                ('balance', models.IntegerField()),
                ('integral', models.IntegerField()),
                ('pwd', models.CharField(max_length=40)),
                ('lev', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('usedays', models.IntegerField()),
                ('v_level', models.IntegerField(blank=True, null=True)),
                ('lasttime', models.CharField(max_length=20)),
                ('isvip', models.TextField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
