create schema if not exists oj;

drop table if exists oj.problem;
create table if not exists oj.problem
(
    id          bigint unsigned auto_increment
        primary key,
    title       varchar(100),
    contributor varchar(100),
    start_time  datetime,
    time_limit  int,
    content     text,
    status      text,
    tag         text,
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

drop table if exists oj.submit;
create table if not exists oj.submit
(
    id          bigint unsigned auto_increment
        primary key,
    problem_id  int,
    user_id     int,
    create_time datetime,
    code        text,
    status      varchar(100),
    returned    text
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
    description text,
    constraint id
        unique (id)
);

drop table if exists oj.private_problem;
create table if not exists oj.private_problem
(
    id         bigint unsigned auto_increment
        primary key,
    title      varchar(100),
    time_limit int,
    content    text,
    tag        text
);

drop table if exists oj.private_submit;
create table if not exists oj.private_submit
(
    id          bigint unsigned auto_increment primary key,
    problem_id  int,
    user_id     int,
    create_time datetime,
    code        text,
    status      varchar(100),
    returned    text
);


drop table if exists oj.enroll;
create table if not exists oj.enroll
(
    id             bigint unsigned auto_increment primary key,
    competition_id int,
    user_id        int,
    join_time      datetime
);

