/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/2/21 11:12:34                           */
/*==============================================================*/


drop table if exists a_charge;

drop table if exists c_a_tag;

drop table if exists c_article;

drop table if exists c_article_tag;

drop table if exists c_images;

drop table if exists c_m_tag;

drop table if exists c_music;

drop table if exists c_music_tag;

drop table if exists comment;

drop table if exists first_images;

drop table if exists first_sentence;

drop table if exists m_ability;

drop table if exists m_charge2;

drop table if exists manager;

drop table if exists t_admin_level;

drop table if exists t_advertising;

drop table if exists t_buy_vip;

drop table if exists t_haveread;

drop table if exists t_level_suffer;

drop table if exists t_message_feedback;

drop table if exists t_slidesshow;

drop table if exists t_task;

drop table if exists t_user_tasks;

drop table if exists t_usermessage;

drop table if exists t_vip_classify;

drop table if exists u_collection;

drop table if exists u_download;

drop table if exists u_fabulous;

drop table if exists u_give_reward;

drop table if exists u_pay_classify;

drop table if exists u_payrank;

drop table if exists user;

/*==============================================================*/
/* Table: a_charge                                              */
/*==============================================================*/
create table a_charge
(
   id                   VARCHAR(50) not null,
   a_id                 VARCHAR(70),
   gold                 INTEGER,
   primary key (id)
);

/*==============================================================*/
/* Table: c_a_tag                                               */
/*==============================================================*/
create table c_a_tag
(
   a_id                 VARCHAR(50) not null,
   t_name               VARCHAR(30),
   primary key (a_id)
);

/*==============================================================*/
/* Table: c_article                                             */
/*==============================================================*/
create table c_article
(
   a_id                 VARCHAR(70) not null,
   i_id                 VARCHAR(50),
   m_id                 VARCHAR(50),
   u_id                 VARCHAR(70) not null,
   name                 VARCHAR(70),
   number               INTEGER,
   status               VARCHAR(5) not null,
   isfree               bit not null,
   fabulous             INTEGER,
   profit               FLOAT,
   details              text,
   date                 VARCHAR(50) not null,
   primary key (a_id)
);

/*==============================================================*/
/* Table: c_article_tag                                         */
/*==============================================================*/
create table c_article_tag
(
   id                   VARCHAR(50) not null,
   t_id                 VARCHAR(50),
   c_a_id               VARCHAR(70),
   primary key (id)
);

/*==============================================================*/
/* Table: c_images                                              */
/*==============================================================*/
create table c_images
(
   i_id                 VARCHAR(50) not null,
   i_name               VARCHAR(50),
   images               longblob,
   link                 VARCHAR(100),
   primary key (i_id)
);

/*==============================================================*/
/* Table: c_m_tag                                               */
/*==============================================================*/
create table c_m_tag
(
   m_id                 VARCHAR(50) not null,
   t_name               VARCHAR(50),
   primary key (m_id)
);

/*==============================================================*/
/* Table: c_music                                               */
/*==============================================================*/
create table c_music
(
   m_id                 VARCHAR(50) not null,
   u_id                 VARCHAR(70) not null,
   m_name               VARCHAR(60),
   lyrics               VARCHAR(50),
   composition          VARCHAR(50),
   music                longblob,
   isfree               bit not null,
   primary key (m_id)
);

/*==============================================================*/
/* Table: c_music_tag                                           */
/*==============================================================*/
create table c_music_tag
(
   id                   VARCHAR(50) not null,
   m_id                 VARCHAR(50),
   c_m_m_id             VARCHAR(50),
   primary key (id)
);

/*==============================================================*/
/* Table: comment                                               */
/*==============================================================*/
create table comment
(
   u_id                 VARCHAR(70),
   a_id                 VARCHAR(70),
   m_id                 VARCHAR(50),
   time                 VARCHAR(20),
   content              text,
   id                   VARCHAR(20) not null,
   primary key (id)
);

/*==============================================================*/
/* Table: first_images                                          */
/*==============================================================*/
create table first_images
(
   img_id               VARCHAR(20) not null,
   link                 VARCHAR(100),
   image                longblob,
   primary key (img_id)
);

/*==============================================================*/
/* Table: first_sentence                                        */
/*==============================================================*/
create table first_sentence
(
   s_id                 VARCHAR(20) not null,
   img_id               VARCHAR(20),
   sentence             text,
   primary key (s_id)
);

/*==============================================================*/
/* Table: m_ability                                             */
/*==============================================================*/
create table m_ability
(
   m_id                 VARCHAR(20) not null,
   m_user               VARCHAR(50),
   m_concent            TEXT,
   m_notice             text,
   m_advertisement      text,
   m_msg                text,
   m_illegal_user       VARCHAR(20),
   m_illegal_content    text,
   primary key (m_id)
);

/*==============================================================*/
/* Table: m_charge2                                             */
/*==============================================================*/
create table m_charge2
(
   id                   VARCHAR(50) not null,
   m_id                 VARCHAR(50),
   gold                 INTEGER,
   primary key (id)
);

/*==============================================================*/
/* Table: manager                                               */
/*==============================================================*/
create table manager
(
   m_id                 varchar(30) not null,
   level                VARCHAR(70),
   m_a_m_id             VARCHAR(20),
   m_account            varchar(30),
   m_pwd                varchar(50),
   m_Email              varchar(40),
   m_telephone          varchar(30),
   m_set                varchar(50),
   primary key (m_id)
);

/*==============================================================*/
/* Table: t_admin_level                                         */
/*==============================================================*/
create table t_admin_level
(
   id                   VARCHAR(70) not null,
   lev                  INTEGER not null,
   category             VARCHAR(20) not null,
   indetail             text,
   primary key (id)
);

/*==============================================================*/
/* Table: t_advertising                                         */
/*==============================================================*/
create table t_advertising
(
   a_id                 VARCHAR(70) not null,
   img_id               VARCHAR(70),
   title                VARCHAR(100) not null,
   text                 VARCHAR(100),
   link                 VARCHAR(100) not null,
   primary key (a_id)
);

/*==============================================================*/
/* Table: t_buy_vip                                             */
/*==============================================================*/
create table t_buy_vip
(
   id                   VARCHAR(70) not null,
   u_id                 VARCHAR(70) not null,
   v_id                 VARCHAR(70),
   open_time            VARCHAR(20) not null,
   primary key (id)
);

/*==============================================================*/
/* Table: t_haveread                                            */
/*==============================================================*/
create table t_haveread
(
   have_id              VARCHAR(70) not null,
   a_id                 VARCHAR(70),
   m_id                 VARCHAR(50),
   u_id                 VARCHAR(70),
   read_time            VARCHAR(20),
   primary key (have_id)
);

/*==============================================================*/
/* Table: t_level_suffer                                        */
/*==============================================================*/
create table t_level_suffer
(
   ID                   VARCHAR(70) not null,
   grade                INTEGER not null,
   experience           INTEGER not null,
   primary key (ID)
);

/*==============================================================*/
/* Table: t_message_feedback                                    */
/*==============================================================*/
create table t_message_feedback
(
   id                   VARCHAR(70) not null,
   u_id                 VARCHAR(70),
   qq                   VARCHAR(20),
   phone                VARCHAR(11),
   content              text not null,
   primary key (id)
);

/*==============================================================*/
/* Table: t_slidesshow                                          */
/*==============================================================*/
create table t_slidesshow
(
   img_id               VARCHAR(70) not null,
   number               INTEGER not null,
   image                longblob not null,
   link                 VARCHAR(100) not null,
   primary key (img_id)
);

/*==============================================================*/
/* Table: t_task                                                */
/*==============================================================*/
create table t_task
(
   task_id              VARCHAR(70) not null,
   name                 VARCHAR(100) not null,
   reward               INTEGER not null default 0,
   description          VARCHAR(100),
   task_type            VARCHAR(20),
   primary key (task_id)
);

/*==============================================================*/
/* Table: t_user_tasks                                          */
/*==============================================================*/
create table t_user_tasks
(
   t_u_id               VARCHAR(70) not null,
   task_id              VARCHAR(70),
   u_id                 VARCHAR(70),
   isfinish             bool,
   finish_time          VARCHAR(50),
   primary key (t_u_id)
);

/*==============================================================*/
/* Table: t_usermessage                                         */
/*==============================================================*/
create table t_usermessage
(
   u_id                 VARCHAR(70),
   title                VARCHAR(50),
   content              text,
   time                 VARCHAR(16),
   id                   VARCHAR(20) not null,
   primary key (id)
);

/*==============================================================*/
/* Table: t_vip_classify                                        */
/*==============================================================*/
create table t_vip_classify
(
   v_id                 VARCHAR(70) not null,
   days                 INTEGER,
   price                INTEGER,
   dis_days             INTEGER,
   whether              BIT not null,
   description          text,
   primary key (v_id)
);

/*==============================================================*/
/* Table: u_collection                                          */
/*==============================================================*/
create table u_collection
(
   collection_id        VARCHAR(50) not null,
   a_id                 VARCHAR(70),
   m_id                 VARCHAR(50),
   u_id                 VARCHAR(70),
   datetime             VARCHAR(50),
   primary key (collection_id)
);

/*==============================================================*/
/* Table: u_download                                            */
/*==============================================================*/
create table u_download
(
   u_id                 VARCHAR(70),
   a_id                 VARCHAR(70),
   m_id                 VARCHAR(50),
   d_id                 VARCHAR(50) not null,
   primary key (d_id)
);

/*==============================================================*/
/* Table: u_fabulous                                            */
/*==============================================================*/
create table u_fabulous
(
   u_id                 VARCHAR(70) not null,
   a_id                 VARCHAR(70),
   m_id                 VARCHAR(50),
   datatime             VARCHAR(20) not null,
   id                   VARCHAR(20) not null,
   primary key (id)
);

/*==============================================================*/
/* Table: u_give_reward                                         */
/*==============================================================*/
create table u_give_reward
(
   u_g_id               VARCHAR(70) not null,
   m_id                 VARCHAR(50),
   a_id                 VARCHAR(70),
   u_id                 VARCHAR(70),
   reward               VARCHAR(70),
   time                 VARCHAR(16),
   primary key (u_g_id)
);

/*==============================================================*/
/* Table: u_pay_classify                                        */
/*==============================================================*/
create table u_pay_classify
(
   pc_id                VARBINARY(70) not null,
   RMB                  INTEGER not null,
   number               INTEGER not null,
   primary key (pc_id)
);

/*==============================================================*/
/* Table: u_payrank                                             */
/*==============================================================*/
create table u_payrank
(
   p_r_id               VARBINARY(70) not null,
   pc_id                VARBINARY(70),
   u_id                 VARCHAR(70),
   time                 VARCHAR(16),
   primary key (p_r_id)
);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user
(
   u_id                 VARCHAR(70) not null,
   name                 VARCHAR(20) not null,
   phone                VARCHAR(11) not null,
   vip_datetime         VARCHAR(20),
   image                VARBINARY(100) not null,
   balance              INTEGER not null default 0,
   integral             INTEGER not null default 0,
   pwd                  VARCHAR(40) not null,
   lev                  INTEGER not null default 1,
   experience           INTEGER not null default 0,
   usedays              INTEGER not null,
   v_level              INTEGER,
   lasttime             VARCHAR(20) not null,
   isvip                bit not null,
   primary key (u_id)
);

alter table a_charge add constraint FK_Reference_20 foreign key (a_id)
      references c_article (a_id) on delete restrict on update restrict;

alter table c_article add constraint FK_Reference_23 foreign key (u_id)
      references user (u_id) on delete restrict on update restrict;

alter table c_article add constraint FK_Reference_6 foreign key (i_id)
      references c_images (i_id) on delete restrict on update restrict;

alter table c_article add constraint FK_Reference_7 foreign key (m_id)
      references c_music (m_id) on delete restrict on update restrict;

alter table c_article_tag add constraint FK_Reference_1 foreign key (t_id)
      references c_a_tag (a_id) on delete restrict on update restrict;

alter table c_article_tag add constraint FK_Reference_2 foreign key (c_a_id)
      references c_article (a_id) on delete restrict on update restrict;

alter table c_music add constraint FK_Reference_24 foreign key (u_id)
      references user (u_id) on delete restrict on update restrict;

alter table c_music_tag add constraint FK_Reference_4 foreign key (c_m_m_id)
      references c_m_tag (m_id) on delete restrict on update restrict;

alter table c_music_tag add constraint FK_Reference_5 foreign key (m_id)
      references c_music (m_id) on delete restrict on update restrict;

alter table comment add constraint FK_Reference_37 foreign key (u_id)
      references user (u_id) on delete restrict on update restrict;

alter table comment add constraint FK_Reference_38 foreign key (a_id)
      references c_article (a_id) on delete restrict on update restrict;

alter table comment add constraint FK_Reference_39 foreign key (m_id)
      references c_music (m_id) on delete restrict on update restrict;

alter table first_sentence add constraint FK_Reference_45 foreign key (img_id)
      references first_images (img_id) on delete restrict on update restrict;

alter table m_charge2 add constraint FK_Reference_21 foreign key (m_id)
      references c_music (m_id) on delete restrict on update restrict;

alter table manager add constraint FK_Reference_41 foreign key (level)
      references t_admin_level (id) on delete restrict on update restrict;

alter table manager add constraint FK_Reference_47 foreign key (m_a_m_id)
      references m_ability (m_id) on delete restrict on update restrict;

alter table t_advertising add constraint FK_Reference_44 foreign key (img_id)
      references t_slidesshow (img_id) on delete restrict on update restrict;

alter table t_buy_vip add constraint FK_Reference_42 foreign key (u_id)
      references user (u_id) on delete restrict on update restrict;

alter table t_buy_vip add constraint FK_Reference_43 foreign key (v_id)
      references t_vip_classify (v_id) on delete restrict on update restrict;

alter table t_haveread add constraint FK_Reference_14 foreign key (a_id)
      references c_article (a_id) on delete restrict on update restrict;

alter table t_haveread add constraint FK_Reference_17 foreign key (m_id)
      references c_music (m_id) on delete restrict on update restrict;

alter table t_haveread add constraint FK_Reference_54 foreign key (u_id)
      references user (u_id) on delete restrict on update restrict;

alter table t_message_feedback add constraint FK_Reference_29 foreign key (u_id)
      references user (u_id) on delete restrict on update restrict;

alter table t_user_tasks add constraint FK_Reference_49 foreign key (task_id)
      references t_task (task_id) on delete restrict on update restrict;

alter table t_user_tasks add constraint FK_Reference_52 foreign key (u_id)
      references user (u_id) on delete restrict on update restrict;

alter table t_usermessage add constraint FK_Reference_28 foreign key (u_id)
      references user (u_id) on delete restrict on update restrict;

alter table u_collection add constraint FK_Reference_15 foreign key (a_id)
      references c_article (a_id) on delete restrict on update restrict;

alter table u_collection add constraint FK_Reference_16 foreign key (m_id)
      references c_music (m_id) on delete restrict on update restrict;

alter table u_collection add constraint FK_Reference_48 foreign key (u_id)
      references user (u_id) on delete restrict on update restrict;

alter table u_download add constraint FK_Reference_25 foreign key (u_id)
      references user (u_id) on delete restrict on update restrict;

alter table u_download add constraint FK_Reference_26 foreign key (a_id)
      references c_article (a_id) on delete restrict on update restrict;

alter table u_download add constraint FK_Reference_27 foreign key (m_id)
      references c_music (m_id) on delete restrict on update restrict;

alter table u_fabulous add constraint FK_Reference_32 foreign key (u_id)
      references user (u_id) on delete restrict on update restrict;

alter table u_fabulous add constraint FK_Reference_33 foreign key (a_id)
      references c_article (a_id) on delete restrict on update restrict;

alter table u_fabulous add constraint FK_Reference_34 foreign key (m_id)
      references c_music (m_id) on delete restrict on update restrict;

alter table u_give_reward add constraint FK_Reference_18 foreign key (m_id)
      references c_music (m_id) on delete restrict on update restrict;

alter table u_give_reward add constraint FK_Reference_19 foreign key (a_id)
      references c_article (a_id) on delete restrict on update restrict;

alter table u_give_reward add constraint FK_Reference_51 foreign key (u_id)
      references user (u_id) on delete restrict on update restrict;

alter table u_payrank add constraint FK_Reference_50 foreign key (pc_id)
      references u_pay_classify (pc_id) on delete restrict on update restrict;

alter table u_payrank add constraint FK_Reference_53 foreign key (u_id)
      references user (u_id) on delete restrict on update restrict;

