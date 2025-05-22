---
layout: post
---
# 坑爹的字符集问题：踩到了 MySQL 的 bug - V2EX
- URL: [原文](https://www.v2ex.com/t/1133409)
- Added At: 2025-05-22 01:19:39
- [Link To Text](_posts/2025-05-22-坑爹的字符集问题：踩到了-mysql-的-bug---v2ex_raw.md)

## TL;DR
在使用`utf8mb4_bin`校对规则的MySQL/OceanBase中，由于换行符小于空格，导致`like 'abc%'`查询在有索引的情况下无法匹配包含换行符的数据。`explain`显示查询被优化为范围查询，但范围计算错误。该问题已报告给MySQL但尚未解决，作者将持续关注并更新进展。


## Summary
1. **问题发现**：同事在MySQL测试中发现使用`like`查询无法匹配到数据。

2. **问题代码**：
   - 创建表结构：`create table t1 ( c1 varchar(16), key idx (c1) ) collate=utf8mb4_bin;`
   - 插入数据：`insert into t1 values ('000\n'), ('123\n'), ('abc\n');`
   - 查询语句：`select * from t1 where c1 like 'abc%';`
   - 预期结果：应该匹配出 `'abc\n'`，但实际查询结果为空。

3. **OceanBase验证**：在OceanBase上执行相同语句，结果也为空。

4. **索引影响**：
   - 删除索引后：`alter table t1 drop index idx;`
   - 再次查询：`select * from t1 where c1 like 'abc%';`
   - 查询结果：成功匹配到 `'abc\n'`，说明索引导致了查询异常。

5. **Explain分析**：
   - 使用`explain format=tree`分析带索引的查询：
     - 查询优化为范围查询：`Covering index range scan on t1 using idx over ('abc' <= c1 <= 'abc?????????????')`
     - 后面的`?`实际是`0xff`。

6. **校对规则**：
   - 设置连接校对规则：`set collation_connection=utf8mb4_bin;`
   - 比较`'abc\n'`和`'abc'`的大小：`select 'abc\n' < 'abc';`
   - 结果显示`'abc\n' < 'abc'`为真，即`'abc\n'`小于`'abc'`。

7. **字符集信息**：
   - 查看`utf8mb4_bin`的校对规则：`show collation like 'utf8mb4_bin';`
   - `Pad_attribute`为`PAD SPACE`，表示长度对齐时补空格。
   - 空格（`0x20`）比换行符（`0x0a`）大。

8. **问题结论**：在`utf8mb4_bin`校对规则下，`'abc\n'`小于`'abc'`，导致`like 'abc%'`的范围查询优化出现问题。

9. **Bug状态**：
   - 已向MySQL提交patch，但未被关注。
   - 其他patch已被合并，但此问题仍然存在。

10. **未来计划**：如果问题得到解决，将会更新进展。

