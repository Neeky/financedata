---- 创建数据库

create database fdb char set utf8;

---- 创建用户
create user appuser@'127.0.0.1' identified by 'Pass@123';
create user appuser@'localhost' identified by 'Pass@123';
create user appuser@'%' identified by 'Pass@123';

grant all on fdb.* to appuser@'127.0.0.1';
grant all on fdb.* to appuser@'localhost';
grant all on fdb.* to appuser@'%';

---- 






