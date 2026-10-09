SQL查询练习
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

