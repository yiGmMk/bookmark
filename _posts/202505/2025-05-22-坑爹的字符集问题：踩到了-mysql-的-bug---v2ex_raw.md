---
layout: post
---
Title: 坑爹的字符集问题：踩到了 MySQL 的 bug - V2EX

URL Source: https://www.v2ex.com/t/1133409

Published Time: 2025-05-22T00:33:27Z

Markdown Content:
昨天的 [/t/1133223](https://www.v2ex.com/t/1133223) 吸引了大家不少的讨论，今天我来说一个工作上遇到的问题。

准确地说，这个问题是 MySQL 字符集中的校对规则出了 BUG ，字符集本身是无辜的。

这个 bug 现在都还在，欢迎大家验证哈。

* * *

故事是这样的。

同事在连 MySQL 库做测试时发现了一个诡异的现象：查不到匹配的数据。

相关语句简化如下（主键等字段已省略）：

```
create table t1 ( c1 varchar(16), key idx (c1) ) collate=utf8mb4_bin;

insert into t1 values ('000\n'), ('123\n'), ('abc\n');

select * from t1 where c1 like 'abc%';
```

这怎么看，都应该匹配出 `'abc\n'`，对吧？

事实情况是：

```
mysql> select * from t1 where c1 like 'abc%';
Empty set (0.00 sec)
```

天塌了，查出来竟然是空的。

然后我拿同样的语句在 OceanBase 上跑了一下，竟然也是空。（两眼一黑）

* * *

可能会有人说，那肯定是你写的语句有问题，或者 utf8mb4_bin 就这样，吧啦吧啦。

那如果这样呢：

```
mysql> alter table t1 drop index idx;
Query OK, 0 rows affected (0.001 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from t1 where c1 like 'abc%';
+------+
| c1   |
+------+
| abc
 |
+------+
1 row in set (0.001 sec)
```

哎，索引删了就好了。

总不能说，加个索引，能把结果集搞没吧。那肯定 bug 了。

* * *

那到底是咋回事呢：带上索引，我们 explain 看一下。

```
mysql> explain format=tree select * from t1 where c1 like 'abc%' \G
*************************** 1. row ***************************
EXPLAIN: -> Filter: (t1.c1 like 'abc%')  (cost=0.46 rows=1)
    -> Covering index range scan on t1 using idx over ('abc' <= c1 <= 'abc?????????????')  (cost=0.46 rows=1)

1 row in set (0.001 sec)
```

原来这个前置匹配，因为有索引，优化为了范围查询。后面的一串 `?` 其实是 `0xff`，没什么问题。

那看下 `'abc\n'` 和 `'abc'` 呢？

```
mysql> set collation_connection=utf8mb4_bin;
Query OK, 0 rows affected (0.000 sec)

mysql> select 'abc\n' < 'abc';
+-----------------+
| 'abc\n' < 'abc' |
+-----------------+
|               1 |
+-----------------+
1 row in set (0.000 sec)
```

再次两眼一黑。我倒，怎么会这样。这是什么排序规则。看下 utf8mb4_bin 吧。

```
mysql> show collation like 'utf8mb4_bin';
+-------------+---------+----+---------+----------+---------+---------------+
| Collation   | Charset | Id | Default | Compiled | Sortlen | Pad_attribute |
+-------------+---------+----+---------+----------+---------+---------------+
| utf8mb4_bin | utf8mb4 | 46 |         | Yes      |       1 | PAD SPACE     |
+-------------+---------+----+---------+----------+---------+---------------+
1 row in set (0.001 sec)
```

`Pad_attribute` 是 `PAD SPACE`，表示对齐长度时，后面补空格。这下就说通了。空格是 `0x20`，换行符是 `0x0a`。`\n` 比 `` 小。

所以！！虽然反直觉，在 utf8mb4_bin 下，`'abc\n'` 就是 `'abc'` 小！

**结论：`like 'abc%'` 的范围查询优化有问题。**

* * *

关于这个 bug ，我已经向 MySQL 提交了 patch ，但是似乎没有得到关注。我看了下更新日志，我提的另一个 patch 已经被合入，但是这个问题依然还在。看来涉及到字符集，这个坑麻烦到他们都不想处理了。

![Image 1](https://i.imgur.com/UASkTDJ.png)_[ 同一时间提交的代码已经合入 ]_

![Image 2](https://i.imgur.com/AUjpBmz.png)_[ 这个问题还是打开的 ]_

* * *

如果哪天他们合入或者解决了，我再 append 新的进展。

