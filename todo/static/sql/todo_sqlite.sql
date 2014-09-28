create table todo(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, finished INTEGER NOT NULL default 0, post_date TEXT);

insert into todo values(4,'增加摘要功能，除标题外还可以写描述', 0, '2011-06-03 06:08:10');
insert into todo values(5,'增加分类，不同的事项划分到不同的分类中去', 0, '2011-06-03 06:08:37');
insert into todo values(6,'增加协作功能，增加用户功能，可以指定转给某个人，且用邮件通知他', 0, '2011-06-03 06:09:18');
insert into todo values(7,'不直接删除，改为完成，标示为该条事项已完成显示在最下方', 0, '2011-06-03 06:09:41');
insert into todo values(8,'这是一条测试', 1, '2011-06-04 23:00:47');
insert into todo values(9,'这是一条测试2', 1, '2011-06-04 23:01:31');
