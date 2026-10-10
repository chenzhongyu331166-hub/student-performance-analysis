SQL练习
-- 查询0：查询表结构
SELECT * FROM performance LIMIT 0;

-- 查询1：查询全部记录（SELECT *）
SELECT * FROM performance;

-- 查询2：按学生编号查询（对应作业：按姓名查询，这里换成student_id，S1000是表里真实存在编号）
SELECT * FROM performance WHERE student_id = 'S1000';

-- 查询3：条件筛选，筛选考试分数 exam_score >= 60 的学生
SELECT * FROM performance WHERE exam_score >= 60;

-- 查询4：排序，按考试分数 exam_score 从高到低排序（ORDER BY DESC）
SELECT * FROM performance ORDER BY exam_score DESC;

-- 查询5：取分数最高前3条（排序+LIMIT）
SELECT * FROM performance ORDER BY exam_score DESC LIMIT 3;

-- 查询6：查询student_id 和exam_score两列，并按exam_score从高到低排序
SELECT student_id, exam_score FROM performance ORDER BY exam_score DESC;

-- insert插入练习
INSERT INTO performance(student_id, exam_score) VALUES ('S1001', 85);

-- update更新练习
UPDATE performance SET exam_score = 90 WHERE student_id = 'S1001';

-- delete删除练习
DELETE FROM performance WHERE student_id = 'S1001';         

-- 修改学生 S9999 的age为 22，同时exam_score改成 88
UPDATE performance SET age=22 ,exam_score=88 WHERE student_id='S9999';

-- ======================
-- 【D15 新增：GROUP BY 分组聚合 3题（基于真实performance表，分组字段：parental_education_level 家长教育水平）】
-- 聚合函数：COUNT / AVG / MAX / MIN / SUM
-- ======================
-- D15-Q1：按家长教育水平分组，每组学生的考试平均分 AVG
SELECT parental_education_level, AVG(exam_score)AS avg_exam_level FROM performance GROUP BY parental_education_level;

-- D15-Q2：按家长教育水平分组，统计每组一共有多少学生 COUNT(*)
SELECT parental_education_level, COUNT(*)AS student_count FROM performance GROUP BY parental_education_level;

-- D15-Q3：按家长教育水平分组，查询每组考试最高分MAX、最低分MIN
SELECT parental_education_level,MAX(exam_score)AS max_exam_score,MIN(exam_score)AS min_exam_score FROM performance GROUP BY parental_education_level;

-- 创建额外信息表 extra_info（仅用于JOIN练习）
CREATE TABLE IF NOT EXISTS extra_info (
    student_id  TEXT PRIMARY KEY,
    hometown    TEXT,
    transport_type TEXT
);
INSERT INTO extra_info(student_id,hometown,transport_type)
VALUES
('S1000','Beijing','Bus'),
('S1001','Shanghai','Subway'),
('S1002','Guangzhou','Car'),
('S1003','Shenzhen','Bike'),
('S1004','Chengdu','Walk');     

-- D15-Q4 INNER JOIN：关联 performance 和 extra_info两张表
-- 注意：当前student.db是只读CSV映射表，无法执行建表、插入，仅用于学习语法
SELECT p.student_id,p.gender,p.exam_score,e.homtown,e.transport_type
FROM performance p
INSERT INTO extra_info e
ON p.student_id = e.student_id;

-- D15拓展：JOIN + GROUP BY，统计不同家乡学生的平均分
SELECT e.hometown,AVG(exam_score)AS avg_score
FROM performance p
JOIN extra_info e
ON p.student_id = e.student_id
GROUP BY e.hometown;

-- D15拓展：LEFT JOIN 演示（左连接，对比INNER JOIN）
-- LEFT JOIN：左边performance表全部行保留，右边extra_info匹配不到时，右边字段为NULL
SELECT p.student_id,p.gender,p.exam_score,e.hometown
FROM performance p
LEFT JOIN extra_info e
ON p.student_id = e.student_id;