create schema if not exists oj;

drop table if exists oj.problem;
create table if not exists oj.problem
(
    id          bigint unsigned auto_increment
        primary key,
    title       varchar(100),
    contributor varchar(100),
    time_limit  int,
    content     text,
    status      text,
    oss_id      int,
    year        text,
    difficulty  text,
    derivation  text,
    constraint id unique (id)
);

drop table if exists oj.user;
create table if not exists oj.user
(
    id          bigint unsigned auto_increment
        primary key,
    username    varchar(100),
    nickname    varchar(100),
    password    varchar(500),
    email       varchar(100),
    create_time datetime,
    level       int,
    constraint id
        unique (id),
    constraint username
        unique (username)
);

drop table if exists oj.user_upload;
create table if not exists oj.user_upload
(
    id         bigint unsigned auto_increment
        primary key,
    user_id    int,
    context_id int,
    oss_id     int,
    grade      int,
    comment    text,
    constraint id
        unique (id)
);

drop table if exists oj.oss;
create table if not exists oj.oss
(
    id      bigint unsigned auto_increment
        primary key,
    user_id int,
    type    text
);

drop table if exists oj.event;
create table if not exists oj.event
(
    id             bigint unsigned auto_increment
        primary key,
    title          varchar(100),
    contributor_id int,
    type           text, # assignment / competition
    start_at       datetime,
    due_at         datetime,
    description    text,
    constraint id
        unique (id)
);

drop table if exists oj.enrollment;
create table if not exists oj.enrollment
(
    id       bigint unsigned auto_increment primary key,
    event_id int,
    user_id  int
);

drop table if exists oj.containing;
create table if not exists oj.containing
(
    id         bigint unsigned auto_increment primary key,
    serial     int,
    event_id   int,
    problem_id int
);


################ check ################

drop table if exists oj.submit;
create table if not exists oj.submit
(
    id          bigint unsigned auto_increment
        primary key,
    problem_id  int,
    user_id     int,
    create_time datetime,
    code        text,
    language    varchar(100),
    status      varchar(100),
    returned    text,
    constraint id
        unique (id)
);



drop table if exists oj.private_problem;
create table if not exists oj.private_problem
(
    id          bigint unsigned auto_increment
        primary key,
    title       varchar(100),
    contributor varchar(100),
    time_limit  int,
    content     text,
    year        text,
    difficulty  text,
    derivation  text,
    constraint id unique (id)
);

drop table if exists oj.competition;
create table if not exists oj.competition
(
    id          bigint unsigned auto_increment
        primary key,
    title       varchar(100),
    contributor varchar(100),
    create_at   datetime,
    start_at    datetime,
    due_at      datetime,
    type        text,
    description text,
    constraint id
        unique (id)
);

drop table if exists oj.private_submit;
create table if not exists oj.private_submit
(
    id                 bigint unsigned auto_increment primary key,
    private_problem_id int,
    user_id            int,
    create_time        datetime,
    code               text,
    language           varchar(100),
    status             varchar(100),
    returned           text
);


