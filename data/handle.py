
# 【第 1 段 / 共 62 段】
# --------------------------------------------------------------------
import numpy as np  #numpy 是python专门处理数学运算的包
import scipy as sp  #scipy 是python专门处理科学运算的包，包含很多算法
import pandas as pd #pandas 是python用来进行数据分析和研究的包，非常适合社会科学工作者

import matplotlib #python 专门用于画图的包
from matplotlib import pyplot as plt
import matplotlib.font_manager as font_manager
import seaborn as sns  #a high-level Python data visualization library based on matplotlib. 
from matplotlib.pyplot import cm



import warnings
warnings.filterwarnings("ignore")
import platform
if platform.system() == "Darwin":
    # 简易设置以让matplotlib能显示中文
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
elif platform.system() == "Windows":
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 简易设置以让matplotlib能显示中文
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
else:
    pass


from collections import Counter, defaultdict # 字典函数，下面会用到



df = pd.read_csv(r'D:\我的作品\D12-pandas读筛排存\data\student_habits_performance.csv', encoding='utf-8') 
# --------任务1：拿到表格，先看基础信息--------
print("=====表格行列数(行数,列数)====")
print(df.shape)

print("\n=====每一列的数据类型====")
print(df.dtypes)

print("\n=====前3行预览数据====")
print(df.head(3))

print("\n=====统计每一列缺失值数量【找脏数据】====")
print(df.isnull().sum())
df.dropna(subset=['parental_education_level'], inplace=True)  ## 在列删除缺失值，直接作用于原数据

print("\n=====确认已清洗数据====")
print(df.shape)


print("\n=====性别英文转中文====")
gender_mapping = {
    'Male': '男性',
    'Female': '女性',
    'Other': '不愿透露'
}
df['gender_cn'] = df['gender'].replace(gender_mapping)
print(df['gender'].value_counts()) # 看性别中文统计

# -----【4.2】part_time_job 兼职 -----
print("\n---- 4.2 兼职字段：英文转中文 ----")
part_time_mapping = {
    'No': '无兼职',
    'Yes': '有兼职'
}
df['part_time_job_cn'] = df['part_time_job'].replace(part_time_mapping)
print("转换结果分布：")
print(df['part_time_job_cn'].value_counts())

# -----【4.3】diet_quality 饮食质量 -----
print("\n---- 4.3 饮食质量字段：英文转中文 ----")
diet_mapping = {
    'Poor': '差',
    'Fair': '一般',
    'Good': '好'
}
df['diet_quality_cn'] = df['diet_quality'].replace(diet_mapping)
print("转换结果分布：")
print(df['diet_quality_cn'].value_counts())

# -----【4.4】parental_education_level 家长教育水平 -----
print("\n---- 4.4 家长教育水平字段：英文转中文 ----")
education_mapping = {
    'High School': '高中',
    'Bachelor': '本科',
    'Master': '硕士'
}
df['parental_education_cn'] = df['parental_education_level'].replace(education_mapping)
print("转换结果分布：")
print(df['parental_education_cn'].value_counts())

# -----【4.5】internet_quality 网络质量 -----
print("\n---- 4.5 网络质量字段：英文转中文 ----")
internet_mapping = {
    'Poor': '差',
    'Average': '中等',
    'Good': '好'
}
df['internet_quality_cn'] = df['internet_quality'].replace(internet_mapping)
print("转换结果分布：")
print(df['internet_quality_cn'].value_counts())

# -----【4.6】extracurricular_participation 课外活动 -----
print("\n---- 4.6 课外活动字段：英文转中文 ----")
extracurricular_mapping = {
    'Yes': '参与',
    'No': '未参与'
}
df['extracurricular_cn'] = df['extracurricular_participation'].replace(extracurricular_mapping)
print("转换结果分布：")
print(df['extracurricular_cn'].value_counts())

# ==========【第5步】总检查：确认所有中文列没有英文残留 ==========
print("\n==========【5】映射结果总检查 ==========")
cn_cols = ['gender_cn', 'part_time_job_cn', 'diet_quality_cn',
           'parental_education_cn', 'internet_quality_cn', 'extracurricular_cn']
for col in cn_cols:
    print(f"{col} 的全部取值：{df[col].unique()}")
print("\n✅ 数据清洗 + 字符串中文标注全部完成！")


print("\n==========【6 连续数字字段：pd.cut分箱分组】==========")

# ----------------------6.1 study_hours_per_day 每日学习时长分组----------------------
print("\n----6.1 每日学习时长分组：0‑3，3‑6，6以上----")
# bins边界：0，3，6，无穷大
bins_study = [0,3,6,float('inf')]
labels_study = ["低学习时长","中学习时长","高学习时长"]
df['study_hours_group'] = pd.cut(
    df['study_hours_per_day'],
    bins=bins_study,
    labels=labels_study,
    right=False
)
print("分组统计：")
print(df['study_hours_group'].value_counts().sort_index()) #sort_index按分组顺序输出，不要乱序

# ----------------------6.2 social_media_hours 社交媒体时长分组----------------------
print("\n----6.2 社交媒体使用时长分组：0‑2，2‑4，4以上----")
bins_social = [0,2,4,float('inf')]
labels_social = ["低使用时长","中使用时长","高使用时长"]
df['social_hours_group'] = pd.cut(
    df['social_media_hours'],
    bins=bins_social,
    labels=labels_social,
    right=False
)
print("分组统计：")
print(df['social_hours_group'].value_counts().sort_index())

# ----------------------6.3 sleep_hours 睡眠时长分组----------------------
print("\n----6.3 睡眠时长分组：0‑6，6‑8，8以上----")
bins_sleep = [0,6,8,float('inf')]
labels_sleep = ["低睡眠时长","中等睡眠时长","高睡眠时长"]
df['sleep_group'] = pd.cut(
    df['sleep_hours'],
    bins=bins_sleep,
    labels=labels_sleep,
    right=False
)
print("分组统计：")
print(df['sleep_group'].value_counts().sort_index())

# ----------------------6.4 exam_score考试成绩分组（最重要！成绩）----------------------
print("\n----6.4 考试分数分组：<60不及格，60‑70及格，70‑80中等，80‑90良好，90‑100优秀----")
bins_score = [0,60,70,80,90,100]
labels_score = ["不及格","及格","中等","良好","优秀"]
df['score_group'] = pd.cut(
    df['exam_score'],
    bins=bins_score,
    labels=labels_score,
    right=False
)
print("成绩分组统计：")
print(df['score_group'].value_counts().sort_index())

print("\n✅全部数字字段分箱分组完成！")
print("查看df现在新增的全部分组列：study_hours_group、social_hours_group、sleep_group、score_group")


# ---------------- handle.py 最后！！----------------
# 全部清洗、中文映射、pd.cut分箱做完之后，输出清洗好的数据
df.to_csv(
    r"D:\我的作品\D12-pandas读筛排存\data\df_cleaned.csv",
    index=False,        # 不要额外多出行号那一列
    encoding="utf-8-sig" # Excel打开中文不乱码
)
print("✅handle.py执行结束，已输出 df_cleaned.csv")