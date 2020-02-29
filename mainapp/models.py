# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ACharge(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    a = models.ForeignKey('CArticle', models.DO_NOTHING, blank=True, null=True)
    gold = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'a_charge'


class CATag(models.Model):
    a_id = models.CharField(primary_key=True, max_length=50)
    t_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_a_tag'


class CArticle(models.Model):
    a_id = models.CharField(primary_key=True, max_length=70)
    i = models.ForeignKey('CImages', models.DO_NOTHING, blank=True, null=True)
    m = models.ForeignKey('CMusic', models.DO_NOTHING, blank=True, null=True)
    u = models.ForeignKey('User', models.DO_NOTHING)
    name = models.CharField(max_length=70, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=5)
    isfree = models.TextField()  # This field type is a guess.
    fabulous = models.IntegerField(blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    date = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'c_article'


class CArticleTag(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    t = models.ForeignKey(CATag, models.DO_NOTHING, blank=True, null=True)
    c_a = models.ForeignKey(CArticle, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_article_tag'


class CImages(models.Model):
    i_id = models.CharField(primary_key=True, max_length=50)
    i_name = models.CharField(max_length=50, blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_images'


class CMTag(models.Model):
    m_id = models.CharField(primary_key=True, max_length=50)
    t_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_m_tag'


class CMusic(models.Model):
    m_id = models.CharField(primary_key=True, max_length=50)
    u = models.ForeignKey('User', models.DO_NOTHING)
    m_name = models.CharField(max_length=60, blank=True, null=True)
    lyrics = models.CharField(max_length=50, blank=True, null=True)
    composition = models.CharField(max_length=50, blank=True, null=True)
    music = models.TextField(blank=True, null=True)
    isfree = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'c_music'


class CMusicTag(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    m = models.ForeignKey(CMusic, models.DO_NOTHING, blank=True, null=True)
    c_m_m = models.ForeignKey(CMTag, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_music_tag'


class Comment(models.Model):
    u = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    a = models.ForeignKey(CArticle, models.DO_NOTHING, blank=True, null=True)
    m = models.ForeignKey(CMusic, models.DO_NOTHING, blank=True, null=True)
    time = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'comment'


class FirstImages(models.Model):
    img_id = models.CharField(primary_key=True, max_length=20)
    link = models.CharField(max_length=100, blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'first_images'


class FirstSentence(models.Model):
    s_id = models.CharField(primary_key=True, max_length=20)
    img = models.ForeignKey(FirstImages, models.DO_NOTHING, blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'first_sentence'


class MAbility(models.Model):
    m_id = models.CharField(primary_key=True, max_length=20)
    m_user = models.CharField(max_length=50, blank=True, null=True)
    m_concent = models.TextField(blank=True, null=True)
    m_notice = models.TextField(blank=True, null=True)
    m_advertisement = models.TextField(blank=True, null=True)
    m_msg = models.TextField(blank=True, null=True)
    m_illegal_user = models.CharField(max_length=20, blank=True, null=True)
    m_illegal_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_ability'


class MCharge2(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    m = models.ForeignKey(CMusic, models.DO_NOTHING, blank=True, null=True)
    gold = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'm_charge2'


class Manager(models.Model):
    m_id = models.CharField(primary_key=True, max_length=30)
    level = models.ForeignKey('TAdminLevel', models.DO_NOTHING, db_column='level', blank=True, null=True)
    m_a_m = models.ForeignKey(MAbility, models.DO_NOTHING, blank=True, null=True)
    m_account = models.CharField(max_length=30, blank=True, null=True)
    m_pwd = models.CharField(max_length=50, blank=True, null=True)
    m_email = models.CharField(db_column='m_Email', max_length=40, blank=True, null=True)  # Field name made lowercase.
    m_telephone = models.CharField(max_length=30, blank=True, null=True)
    m_set = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager'


class TAdminLevel(models.Model):
    id = models.CharField(primary_key=True, max_length=70)
    lev = models.IntegerField()
    category = models.CharField(max_length=20)
    indetail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_admin_level'


class TAdvertising(models.Model):
    a_id = models.CharField(primary_key=True, max_length=70)
    img = models.ForeignKey('TSlidesshow', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=100)

    states = (
        (0, '审核中'),
        (1, '已通过'),
        (2, '未通过')
    )
    state = models.IntegerField(choices=states, default=0)

    @property
    def state_label(self):
        return self.states[self.state][-1]

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(TAdvertising, self).save()

    class Meta:
        managed = False
        db_table = 't_advertising'


class TBuyVip(models.Model):
    id = models.CharField(primary_key=True, max_length=70)
    u = models.ForeignKey('User', models.DO_NOTHING)
    v = models.ForeignKey('TVipClassify', models.DO_NOTHING, blank=True, null=True)
    open_time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 't_buy_vip'


class THaveread(models.Model):
    have_id = models.CharField(primary_key=True, max_length=70)
    a = models.ForeignKey(CArticle, models.DO_NOTHING, blank=True, null=True)
    m = models.ForeignKey(CMusic, models.DO_NOTHING, blank=True, null=True)
    u = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    read_time = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_haveread'


class TLevelSuffer(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=70)  # Field name made lowercase.
    grade = models.IntegerField()
    experience = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_level_suffer'


class TMessageFeedback(models.Model):
    id = models.CharField(primary_key=True, max_length=70)
    u = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    qq = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 't_message_feedback'


class TSlidesshow(models.Model):
    img_id = models.CharField(primary_key=True, max_length=70)
    number = models.IntegerField()
    image = models.TextField()
    link = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_slidesshow'


class TSysMenu(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    ord = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_menu'


class TSysRole(models.Model):
    name = models.CharField(unique=True, max_length=20)
    code = models.CharField(unique=True, max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_role'


class TSysRoleMenu(models.Model):
    role_id = models.IntegerField(blank=True, null=True)
    menu_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_role_menu'


class TSysUser(models.Model):
    username = models.CharField(unique=True, max_length=20)
    auth_string = models.CharField(max_length=82)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_user'


class TTask(models.Model):
    task_id = models.CharField(primary_key=True, max_length=70)
    name = models.CharField(max_length=100)
    reward = models.IntegerField()
    description = models.CharField(max_length=100, blank=True, null=True)
    task_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_task'


class TUserTasks(models.Model):
    t_u_id = models.CharField(primary_key=True, max_length=70)
    task = models.ForeignKey(TTask, models.DO_NOTHING, blank=True, null=True)
    u = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    isfinish = models.IntegerField(blank=True, null=True)
    finish_time = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_tasks'


class TUsermessage(models.Model):
    u = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=16, blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 't_usermessage'


class TVipClassify(models.Model):
    v_id = models.CharField(primary_key=True, max_length=70)
    days = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    dis_days = models.IntegerField(blank=True, null=True)
    whether = models.TextField()  # This field type is a guess.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_vip_classify'


class UCollection(models.Model):
    collection_id = models.CharField(primary_key=True, max_length=50)
    a = models.ForeignKey(CArticle, models.DO_NOTHING, blank=True, null=True)
    m = models.ForeignKey(CMusic, models.DO_NOTHING, blank=True, null=True)
    u = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datetime = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'u_collection'


class UDownload(models.Model):
    u = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    a = models.ForeignKey(CArticle, models.DO_NOTHING, blank=True, null=True)
    m = models.ForeignKey(CMusic, models.DO_NOTHING, blank=True, null=True)
    d_id = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'u_download'


class UFabulous(models.Model):
    u = models.ForeignKey('User', models.DO_NOTHING)
    a = models.ForeignKey(CArticle, models.DO_NOTHING, blank=True, null=True)
    m = models.ForeignKey(CMusic, models.DO_NOTHING, blank=True, null=True)
    datatime = models.CharField(max_length=20)
    id = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'u_fabulous'


class UGiveReward(models.Model):
    u_g_id = models.CharField(primary_key=True, max_length=70)
    m = models.ForeignKey(CMusic, models.DO_NOTHING, blank=True, null=True)
    a = models.ForeignKey(CArticle, models.DO_NOTHING, blank=True, null=True)
    u = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    reward = models.CharField(max_length=70, blank=True, null=True)
    time = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'u_give_reward'


class UPayClassify(models.Model):
    pc_id = models.CharField(primary_key=True, max_length=70)
    rmb = models.IntegerField(db_column='RMB')  # Field name made lowercase.
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'u_pay_classify'


class UPayrank(models.Model):
    p_r_id = models.CharField(primary_key=True, max_length=70)
    pc = models.ForeignKey(UPayClassify, models.DO_NOTHING, blank=True, null=True)
    u = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    time = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'u_payrank'


class User(models.Model):
    u_id = models.CharField(primary_key=True, max_length=70)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    vip_datetime = models.CharField(max_length=20, blank=True, null=True)
    image = models.CharField(max_length=100)
    balance = models.IntegerField()
    integral = models.IntegerField()
    pwd = models.CharField(max_length=40)
    lev = models.IntegerField()
    experience = models.IntegerField()
    usedays = models.IntegerField()
    v_level = models.IntegerField(blank=True, null=True)
    lasttime = models.CharField(max_length=20)
    isvip = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'user'
