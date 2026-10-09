import pandas as pd
import sqlite3

# 1.读取csv
df = pd.read_csv(r"D:\我的作品\中学生学业成绩相关影响因素研究\data\student_habits_performance.csv")

# 2.连接sqlite，数据库文件叫 student.db
conn = sqlite3.connect("student.db")

# 3.写入数据库，表名：performance
df.to_sql("performance", conn, if_exists="replace", index=False)

conn.close()
print("导入完成！表名 performance")