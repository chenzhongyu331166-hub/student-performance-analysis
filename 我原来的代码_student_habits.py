# ======================================================================
# 完整 62 段（备份用，别整份丢给豆包，太长）
# 来源：student-habits-vs-academic-performance-ml-90.ipynb
# ======================================================================


# --------------------------------------------------------------------
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

# --------------------------------------------------------------------
# 【第 2 段 / 共 62 段】
# --------------------------------------------------------------------
df = pd.read_csv('C:\\Users\\Administrator\Downloads\\student-habits-vs-academic-performance-ml-90\\student_habits_performance.csv')

# --------------------------------------------------------------------
# 【第 3 段 / 共 62 段】
# --------------------------------------------------------------------
df.shape #列的形状

# --------------------------------------------------------------------
# 【第 4 段 / 共 62 段】
# --------------------------------------------------------------------
df.dtypes #列的数据类型

# --------------------------------------------------------------------
# 【第 5 段 / 共 62 段】
# --------------------------------------------------------------------
df.info() #列的总和

# --------------------------------------------------------------------
# 【第 6 段 / 共 62 段】
# --------------------------------------------------------------------
df.head(5)

# --------------------------------------------------------------------
# 【第 7 段 / 共 62 段】
# --------------------------------------------------------------------
df.isnull().sum() #缺失值

# --------------------------------------------------------------------
# 【第 8 段 / 共 62 段】
# --------------------------------------------------------------------
df.dropna()

# --------------------------------------------------------------------
# 【第 9 段 / 共 62 段】
# --------------------------------------------------------------------
df.dropna(subset=['parental_education_level'], inplace=True)  ## 在列删除缺失值，直接作用于原数据

# --------------------------------------------------------------------
# 【第 10 段 / 共 62 段】
# --------------------------------------------------------------------
df.shape

# --------------------------------------------------------------------
# 【第 11 段 / 共 62 段】
# --------------------------------------------------------------------
df['gender'].unique()

# --------------------------------------------------------------------
# 【第 12 段 / 共 62 段】
# --------------------------------------------------------------------
# 定义性别映射字典
gender_mapping = {
    'Male': '男性',
    'Female': '女性',
    'Other': '不愿透露'
}

# 应用替换（假设您的DataFrame名为 df）
df['gender'] = df['gender'].replace(gender_mapping)

# 验证结果
print(df['gender'].value_counts())

# --------------------------------------------------------------------
# 【第 13 段 / 共 62 段】
# --------------------------------------------------------------------
# 设置图表尺寸和样式
plt.figure(figsize=(8, 6), dpi=100)  # 增大画布尺寸
ax = plt.gca()

# 获取数据
x = df['gender']
labels, counts = np.unique(x, return_counts=True)

# 绘制条形图（调整条宽和间距）
bars = ax.bar(labels, counts, 
             width=0.6,      # 缩小条宽
             color=['#1f77b4', '#ff7f0e', '#2ca02c'],  # 自定义颜色
             edgecolor='black')

# 设置标签和标题（增大字体）
ax.set_title("性别分布", fontsize=16, pad=20)  # pad增加标题间距
ax.set_ylabel("频次", fontsize=14)
ax.set_xlabel("性别", fontsize=14)

# 优化刻度标签
ax.set_xticks(np.arange(len(labels)))  # 确保刻度居中
ax.set_xticklabels(labels, 
                  rotation=45,         # 旋转45度避免重叠
                  ha='right',          # 对齐方式
                  fontsize=12)

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=12)

# 自动调整布局
plt.tight_layout()  # 解决标签截断问题

# 显示图表
plt.show()

# --------------------------------------------------------------------
# 【第 14 段 / 共 62 段】
# --------------------------------------------------------------------
df['study_hours_per_day'].unique()

# --------------------------------------------------------------------
# 【第 15 段 / 共 62 段】
# --------------------------------------------------------------------


# 定义分组边界和标签
bins = [0, 3, 6, float('inf')]  # 0-3小时为低，3-6为中，6+为高
labels = ['低学习时长', '中学习时长', '高学习时长']

# 创建分组列
df['study_hours_group'] = pd.cut(
    df['study_hours_per_day'],
    bins=bins,
    labels=labels,
    right=False  # 左闭右开区间（例如 [3,6)）
)

# 验证分组结果
print(df['study_hours_group'].value_counts().sort_index())

# --------------------------------------------------------------------
# 【第 16 段 / 共 62 段】
# --------------------------------------------------------------------

# 设置中文字体（根据系统选择）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Songti SC']  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 绘制分布图（使用Seaborn简化代码）
plt.figure(figsize=(8, 5))
ax = sns.countplot(x='study_hours_group', data=df, 
                  order=['低学习时长', '中学习时长', '高学习时长'],
                  palette='pastel')

plt.title("学习时长分组分布")
plt.xlabel("学习时长组别")
plt.ylabel("人数")

# 自动调整布局
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# 【第 17 段 / 共 62 段】
# --------------------------------------------------------------------
df['social_media_hours'].unique()

# --------------------------------------------------------------------
# 【第 18 段 / 共 62 段】
# --------------------------------------------------------------------
# 定义分组边界和标签
bins = [0, 2, 4, float('inf')]  # 0-3小时为低，3-6为中，6+为高
labels = ['低使用时长', '中使用时长', '高使用时长']

# 创建分组列
df['social_hours_group'] = pd.cut(
    df['social_media_hours'],
    bins=bins,
    labels=labels,
    right=False  # 左闭右开区间（例如 [3,6)）
)

# 验证分组结果
print(df['social_hours_group'].value_counts().sort_index())

# --------------------------------------------------------------------
# 【第 19 段 / 共 62 段】
# --------------------------------------------------------------------
plt.figure(figsize=(8, 5))

# 绘制分组分布图
ax = sns.countplot(
    x='social_hours_group',
    data=df,
    order=['低使用时长', '中使用时长', '高使用时长'],  # 强制排序
    palette='Set2'  # 使用柔和配色
)

# 设置标题和标签
plt.title("社交软件使用时长分组分布", fontsize=14, pad=12)
plt.xlabel("使用时长分组", fontsize=12)
plt.ylabel("人数", fontsize=12)

# 自动调整布局
plt.tight_layout()

# 显示图表
plt.show()

# --------------------------------------------------------------------
# 【第 20 段 / 共 62 段】
# --------------------------------------------------------------------
df['netflix_hours'].unique()

# --------------------------------------------------------------------
# 【第 21 段 / 共 62 段】
# --------------------------------------------------------------------
# 定义分组边界和标签（与social_media_hours一致）
bins = [0, 1.5, 3.0, float('inf')]  # 0-2小时为低，2-4为中，4+为高
labels = ['低使用时长', '中使用时长', '高使用时长']

# 创建分组列
df['netflix_hours_group'] = pd.cut(
    df['netflix_hours'],
    bins=bins,
    labels=labels,
    right=False  # 左闭右开区间
)

# 验证分组结果
print("Netflix使用分组统计:\n", df['netflix_hours_group'].value_counts().sort_index())

# 画图代码（与社交软件使用分布图一致）
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体（根据系统选择）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Songti SC']  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 绘制分布图
plt.figure(figsize=(8, 5))
ax = sns.countplot(
    x='netflix_hours_group',
    data=df,
    order=labels,
    palette='Set2'
)

# 添加数据标签
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom',
                xytext=(0, 3),
                textcoords='offset points',
                fontsize=12)

plt.title("Netflix使用时长分组分布", fontsize=14)
plt.xlabel("使用时长分组", fontsize=12)
plt.ylabel("人数", fontsize=12)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# 【第 22 段 / 共 62 段】
# --------------------------------------------------------------------
df['part_time_job'].unique()

# --------------------------------------------------------------------
# 【第 23 段 / 共 62 段】
# --------------------------------------------------------------------
# 定义兼职工作映射字典
part_time_mapping = {
    'No': '无兼职',
    'Yes': '有兼职'
}

# 应用中文标签转换
df['part_time_job_cn'] = df['part_time_job'].replace(part_time_mapping)

# 验证结果
print(df['part_time_job_cn'].value_counts())

# --------------------------------------------------------------------
# 【第 24 段 / 共 62 段】
# --------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体（根据系统选择）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Songti SC']  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 绘制分布图
plt.figure(figsize=(8, 5))
ax = sns.countplot(
    x='part_time_job_cn',
    data=df,
    order=['无兼职', '有兼职'],  # 固定顺序
    palette=['#1f77b4', '#ff7f0e']  # 与性别图配色风格一致
)

# 添加数据标签
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom',
                xytext=(0, 3),
                textcoords="offset points",
                fontsize=12)

# 设置标题和标签
plt.title("兼职工作分布", fontsize=14)
plt.xlabel("是否兼职", fontsize=12)
plt.ylabel("人数", fontsize=12)

# 调整布局
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# 【第 25 段 / 共 62 段】
# --------------------------------------------------------------------
df['attendance_percentage'].unique()

# --------------------------------------------------------------------
# 【第 26 段 / 共 62 段】
# --------------------------------------------------------------------
# 定义分组边界和标签（固定分界，无需数据计算）
bins = [0, 75, 90, 100]  # 左闭右开区间
labels = ['低出勤率', '中出勤率', '高出勤率']

# 创建分组列
df['attendance_group'] = pd.cut(
    df['attendance_percentage'],
    bins=bins,
    labels=labels,
    right=False  # 确保75% ≤ 中出勤率 <90%
)

# 验证分组
print("分组标准：<75%为低，75%~90%为中，≥90%为高")
print(df['attendance_group'].value_counts().sort_index())

# 画图代码（与兼职分布图风格完全一致）
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体（根据系统选择）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Songti SC']  # Mac
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(8, 5))
ax = sns.countplot(
    x='attendance_group',
    data=df,
    order=labels,
    palette='Set2',  # 与社交软件使用分组配色一致
    edgecolor='black'
)

# 添加数据标签（格式与之前完全一致）
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom',
                xytext=(0, 3),
                textcoords="offset points",
                fontsize=12)

plt.title("出勤率分组分布（固定标准）", fontsize=14)
plt.xlabel("出勤率组别", fontsize=12)
plt.ylabel("人数", fontsize=12)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# 【第 27 段 / 共 62 段】
# --------------------------------------------------------------------
df['sleep_hours'].unique()

# --------------------------------------------------------------------
# 【第 28 段 / 共 62 段】
# --------------------------------------------------------------------
# 定义分组边界和标签
bins = [0, 6, 8, float('inf')]
labels = ['低睡眠时长', '中等睡眠时长', '高睡眠时长']

# 创建分组列
df['sleep_group'] = pd.cut(
    df['sleep_hours'],
    bins=bins,
    labels=labels,
    right=False  # 左闭右开区间（例如7 ≤ 时长 <9）
)

# 验证分组结果
print("分组统计:\n", df['sleep_group'].value_counts().sort_index())

# --------------------------------------------------------------------
# 【第 29 段 / 共 62 段】
# --------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Songti SC']  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 绘制分布图
plt.figure(figsize=(8, 5))
ax = sns.countplot(
    x='sleep_group',
    data=df,
    order=labels,
    palette='Set2',  # 保持统一配色
    edgecolor='black'
)

# 添加数据标签
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom',
                xytext=(0, 3),
                textcoords="offset points",
                fontsize=12)

plt.title("每日睡眠时长分组分布（优化版）", fontsize=14)
plt.xlabel("睡眠组别", fontsize=12)
plt.ylabel("人数", fontsize=12)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# 【第 30 段 / 共 62 段】
# --------------------------------------------------------------------
df['diet_quality'].unique()

# --------------------------------------------------------------------
# 【第 31 段 / 共 62 段】
# --------------------------------------------------------------------
# 定义饮食质量映射字典
diet_mapping = {
    'Poor': '差',
    'Fair': '一般',
    'Good': '好'
}

# 应用中文标签
df['diet_quality_cn'] = df['diet_quality'].replace(diet_mapping)

# 验证转换结果
print(df['diet_quality_cn'].value_counts())

# --------------------------------------------------------------------
# 【第 32 段 / 共 62 段】
# --------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体（根据系统选择）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Songti SC']  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 绘制分布图
plt.figure(figsize=(8, 5))
ax = sns.countplot(
    x='diet_quality_cn',
    data=df,
    order=['差', '一般', '好'],  # 固定顺序：质量从低到高
    palette='Set2',            # 与兼职、出勤率分组配色一致
    edgecolor='black'
)

# 添加数据标签（格式与之前完全一致）
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom',
                xytext=(0, 3),
                textcoords="offset points",
                fontsize=12)

# 设置标题和标签
plt.title("饮食质量分布", fontsize=14)
plt.xlabel("饮食质量", fontsize=12)
plt.ylabel("人数", fontsize=12)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# 【第 33 段 / 共 62 段】
# --------------------------------------------------------------------
df['exercise_frequency'].unique()

# --------------------------------------------------------------------
# 【第 34 段 / 共 62 段】
# --------------------------------------------------------------------
# 定义分组边界和标签
bins = [-1, 2, 4, 6]  # 左闭右开区间（-1用于包含0值）
labels = ['低锻炼频率', '中锻炼频率', '高锻炼频率']

# 创建分组列
df['exercise_group'] = pd.cut(
    df['exercise_frequency'],
    bins=bins,
    labels=labels,
    right=False
)

# 验证分组
print("分组统计:\n", df['exercise_group'].value_counts().sort_index())

# --------------------------------------------------------------------
# 【第 35 段 / 共 62 段】
# --------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体（根据系统选择）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Songti SC']  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 绘制分布图
plt.figure(figsize=(8, 5))
ax = sns.countplot(
    x='exercise_group',
    data=df,
    order=labels,
    palette='Set2',  # 与饮食质量、出勤率分组配色一致
    edgecolor='black'
)

# 添加数据标签
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom',
                xytext=(0, 3),
                textcoords="offset points",
                fontsize=12)

plt.title("每周锻炼频率分组分布", fontsize=14)
plt.xlabel("锻炼频率组别", fontsize=12)
plt.ylabel("人数", fontsize=12)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# 【第 36 段 / 共 62 段】
# --------------------------------------------------------------------
df['parental_education_level'].unique()

# --------------------------------------------------------------------
# 【第 37 段 / 共 62 段】
# --------------------------------------------------------------------
# 定义教育水平映射字典
education_mapping = {
    'High School': '高中',
    'Bachelor': '本科',
    'Master': '硕士'
}

# 应用中文标签
df['parental_education_cn'] = df['parental_education_level'].replace(education_mapping)

# 验证转换结果
print(df['parental_education_cn'].value_counts())

# --------------------------------------------------------------------
# 【第 38 段 / 共 62 段】
# --------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体（根据系统选择）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Songti SC']  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 绘制分布图（按教育水平从低到高排序）
plt.figure(figsize=(8, 5))
ax = sns.countplot(
    x='parental_education_cn',
    data=df,
    order=['高中', '本科', '硕士'],  # 强制排序：学历从低到高
    palette='Set2',               # 与饮食质量、出勤率配色一致
    edgecolor='black'
)

# 添加数据标签（格式与之前完全一致）
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom',
                xytext=(0, 3),
                textcoords="offset points",
                fontsize=12)

# 设置标题和标签
plt.title("家长教育水平分布", fontsize=14)
plt.xlabel("教育水平", fontsize=12)
plt.ylabel("人数", fontsize=12)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# 【第 39 段 / 共 62 段】
# --------------------------------------------------------------------
df['internet_quality'].unique()

# --------------------------------------------------------------------
# 【第 40 段 / 共 62 段】
# --------------------------------------------------------------------
# 定义网络质量映射字典
internet_mapping = {
    'Poor': '差',
    'Average': '中等',
    'Good': '好'
}

# 应用中文标签
df['internet_quality_cn'] = df['internet_quality'].replace(internet_mapping)

# 验证转换结果（按质量从低到高排序）
print(df['internet_quality_cn'].value_counts().reindex(['差', '中等', '好']))

# --------------------------------------------------------------------
# 【第 41 段 / 共 62 段】
# --------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体（根据系统选择）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Songti SC']  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 绘制分布图
plt.figure(figsize=(8, 5))
ax = sns.countplot(
    x='internet_quality_cn',
    data=df,
    order=['差', '中等', '好'],  # 按质量从低到高排序
    palette='Set2',            # 与饮食质量、家长教育水平配色一致
    edgecolor='black'
)

# 添加数据标签（格式与之前完全一致）
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom',
                xytext=(0, 3),
                textcoords="offset points",
                fontsize=12)

# 设置标题和标签
plt.title("网络质量分布", fontsize=14)
plt.xlabel("网络质量", fontsize=12)
plt.ylabel("人数", fontsize=12)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# 【第 42 段 / 共 62 段】
# --------------------------------------------------------------------
df['mental_health_rating'].unique()

# --------------------------------------------------------------------
# 【第 43 段 / 共 62 段】
# --------------------------------------------------------------------
# 定义分组边界和标签
bins = [0, 4, 7, 11]  # 左闭右开区间
labels = ['低心理健康', '中等心理健康', '高心理健康']

# 创建分组列
df['mental_health_group'] = pd.cut(
    df['mental_health_rating'],
    bins=bins,
    labels=labels,
    right=False  # 确保4分属于低分组，7分属于中等组
)

# 验证分组
print("分组统计:\n", df['mental_health_group'].value_counts().sort_index())

# --------------------------------------------------------------------
# 【第 44 段 / 共 62 段】
# --------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体（根据系统选择）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Songti SC']  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 绘制分布图
plt.figure(figsize=(8, 5))
ax = sns.countplot(
    x='mental_health_group',
    data=df,
    order=labels,
    palette='Set2',  # 与饮食质量、网络质量分组配色一致
    edgecolor='black'
)

# 添加数据标签（格式与之前完全一致）
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom',
                xytext=(0, 3),
                textcoords="offset points",
                fontsize=12)

# 设置标题和标签
plt.title("心理健康评分分组分布", fontsize=14)
plt.xlabel("心理健康组别", fontsize=12)
plt.ylabel("人数", fontsize=12)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# 【第 45 段 / 共 62 段】
# --------------------------------------------------------------------
df['extracurricular_participation'].unique()

# --------------------------------------------------------------------
# 【第 46 段 / 共 62 段】
# --------------------------------------------------------------------
# 定义课外活动参与映射字典
extracurricular_mapping = {
    'Yes': '参与',
    'No': '未参与'
}

# 应用中文标签
df['extracurricular_cn'] = df['extracurricular_participation'].replace(extracurricular_mapping)

# 验证转换结果
print(df['extracurricular_cn'].value_counts())

# --------------------------------------------------------------------
# 【第 47 段 / 共 62 段】
# --------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体（根据系统选择）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Songti SC']  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 绘制分布图
plt.figure(figsize=(8, 5))
ax = sns.countplot(
    x='extracurricular_cn',
    data=df,
    order=['未参与', '参与'],  # 固定顺序：未参与在前
    palette=['#1f77b4', '#ff7f0e'],  # 与兼职工作图配色一致
    edgecolor='black'
)

# 添加数据标签（格式与兼职分布图完全一致）
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom',
                xytext=(0, 3),
                textcoords="offset points",
                fontsize=12)

# 设置标题和标签
plt.title("课外活动参与情况分布", fontsize=14)
plt.xlabel("是否参与课外活动", fontsize=12)
plt.ylabel("人数", fontsize=12)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# 【第 48 段 / 共 62 段】
# --------------------------------------------------------------------
df['exam_score'].unique()

# --------------------------------------------------------------------
# 【第 49 段 / 共 62 段】
# --------------------------------------------------------------------
import pandas as pd
import numpy as np

# 定义分组边界（基于百分位数优化）
bins = [0, 60, 70, 80, 90, 100]  # 常规教育分段优化
labels = ['不及格', '及格', '中等', '良好', '优秀']

# 创建分组列
df['score_group'] = pd.cut(
    df['exam_score'],
    bins=bins,
    labels=labels,
    right=False  # 左闭右开（例如60分属于及格组）
)

# 验证分组
print("分组统计:\n", df['score_group'].value_counts().sort_index())

# --------------------------------------------------------------------
# 【第 50 段 / 共 62 段】
# --------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体（根据系统选择）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Songti SC']  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 绘制分布图
plt.figure(figsize=(10, 6))
ax = sns.countplot(
    x='score_group',
    data=df,
    order=labels,
    palette='viridis',  # 颜色渐变增强可读性
    edgecolor='black'
)

# 添加数据标签
for p in ax.patches:
    ax.annotate(f'{p.get_height()}',
                (p.get_x() + p.get_width()/2, p.get_height()),
                ha='center', va='bottom',
                xytext=(0, 5),
                textcoords="offset points",
                fontsize=12)

# 设置标题和标签
plt.title("考试成绩分组分布", fontsize=16, pad=20)
plt.xlabel("成绩组别", fontsize=14)
plt.ylabel("人数", fontsize=14)

# 优化刻度标签
plt.xticks(fontsize=12)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------
# 【第 51 段 / 共 62 段】
# --------------------------------------------------------------------

# 复制数据（根据实际列名调整）
num_df = df.copy()

# 删除非数值型或不需要的列
num_df.drop(['age', 'student_id', ], axis=1, inplace=True)

num_df.head()

# --------------------------------------------------------------------
# 【第 52 段 / 共 62 段】
# --------------------------------------------------------------------
corrMatrix = num_df.select_dtypes(include=[np.number]).corr() #相关系数矩阵
corrMatrix

# --------------------------------------------------------------------
# 【第 53 段 / 共 62 段】
# --------------------------------------------------------------------
fig = plt.figure(dpi=100,figsize=[9,8])
sns.heatmap(corrMatrix, annot=True,fmt='.2f')#,cmap='Reds'
plt.show()

# --------------------------------------------------------------------
# 【第 54 段 / 共 62 段】
# --------------------------------------------------------------------
mask = np.triu(corrMatrix.corr()) # 新建一个mask,  np.triu() returns the lower triangle of any matrix

fig = plt.figure(dpi=100,figsize=[9,8])
sns.heatmap(corrMatrix, annot=True, mask=mask)
plt.show()

# --------------------------------------------------------------------
# 【第 55 段 / 共 62 段】
# --------------------------------------------------------------------
def difference(contingency):  #计算每个单元格的(实际-期望)^2/期望的差值，同时标注正负号，并用热力图展示
    exp_values = []
    total_n = np.sum(contingency.sum()) # 总样本量 n
    rows= contingency.sum(1).values  #行和
    columns = contingency.sum(0).values #列和
    for r in rows:
        rowv = []
        for c in columns:
            rowv.append(np.round(r*c/total_n,2))
        exp_values.append(rowv)
    contingency_expected = pd.DataFrame(exp_values,columns=contingency.columns,index=contingency.index)
    ct_ = contingency - contingency_expected
    sign_matrix = ct_.le(0).astype(int)*-1+ct_.ge(0).astype(int)
    ct = sign_matrix*(contingency - contingency_expected)*(contingency - contingency_expected)/np.array(contingency_expected)
    figurelength = 5
    if ct.shape[0]/ct.shape[1]>3:
        figurelength=10
    fig = plt.figure(dpi=100,figsize=[5,figurelength])
    sns.heatmap(ct, annot=True,fmt='.1f',cmap="YlGnBu") #fmt 可以调整展示数值是整数，'d'，还是小数 :例如 '.2f' 表示小数点后2位, 试一试'.2g',
    plt.title("$\\frac{(Observed - Expected)^2}{Expected} \: with \: sign$")
    plt.show()

# 功能函数，方便判断结果
def HypothesisTest(H0,siglevel,pvalue): 
    if pvalue<siglevel: #如果p值小于显著性水平，则拒绝原假设
        print("在%s的显著性水平上，拒绝%s这一原假设"%(siglevel,H0))
    else: #反之，则不拒绝原假设。
        print("在%s的显著性水平上，不能拒绝%s这一原假设"%(siglevel,H0))

# --------------------------------------------------------------------
# 【第 56 段 / 共 62 段】
# --------------------------------------------------------------------
import pandas as pd
import numpy as np
from scipy import stats as sp
# 定义需要检验的变量列表（根据实际列名调整）
variables_to_test = [
    'gender',               # 性别
    'study_hours_group',    # 学习时长分组
    'social_media_hours',   # 社交媒体使用时长（已分箱）
    'netflix_hours',        # 流媒体使用时长（已分箱）
    'part_time_job',        # 兼职
    'attendance_group',     # 出勤率分组
    'sleep_group',          # 睡眠分组
    'diet_quality',         # 饮食质量
    'exercise_frequency',   # 锻炼频率（已分箱）
    'parental_education_level', # 家长教育水平
    'internet_quality',     # 网络质量
    'mental_health_group',  # 心理健康分组
    'extracurricular_participation' # 课外活动参与
]

# 创建结果存储表
results = pd.DataFrame(columns=['变量名', '卡方值', 'p值', '自由度', '结论'])

# 显著性水平设置
sig_level = 0.01

for var in variables_to_test:
    try:
        # 生成交叉表
        contingency = pd.crosstab(df[var], df['exam_score'])
      
        # 执行卡方检验
        chi2, p, dof, _ = sp.chi2_contingency(contingency)
      
        # 计算效应量Cramer's V
        n = contingency.sum().sum()
        cramers_v = np.sqrt(chi2 / (n * (min(contingency.shape)-1)))
      
        # 判断结论
        conclusion = "与成绩不独立" if p < sig_level else "与成绩独立" 
      
        # 存储结果
        results = pd.concat([results, pd.DataFrame([{
            '变量名': var,
            '卡方值': round(chi2, 2),
            'p值': round(p, 4),
            '自由度': dof,
            '效应量(Cramers V)': round(cramers_v, 2),
            '结论': conclusion
        }])], ignore_index=True)
      
    except ValueError as e:
        print(f"变量 {var} 检验失败: {str(e)}")
        continue

# 格式优化输出
def highlight_significant(row):
    color = 'red' if row['p值'] < sig_level else 'black'
    return [f'color: {color}' for _ in row]

results.style\
    .format({'卡方值': "{:.2f}", 'p值': "{:.4f}", '效应量(Cramers V)': "{:.2f}"})\
    .apply(highlight_significant, axis=1)\
    .set_caption(f"变量与成绩独立性检验结果 (α={sig_level})")

# --------------------------------------------------------------------
# 【第 57 段 / 共 62 段】
# --------------------------------------------------------------------
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns
import scipy 
import pandas as pd
from collections import Counter

# --------------------------------------------------------------------
# 【第 58 段 / 共 62 段】
# --------------------------------------------------------------------


# ===== 参数设置 =====
alpha = 0.01  # 显著性水平
variables = [
    'gender', 'study_hours_group', 'social_media_hours',
    'part_time_job', 'attendance_group', 'sleep_group',
    'diet_quality', 'exercise_group', 'parental_education_level',
    'internet_quality', 'mental_health_group',
    'extracurricular_participation'
]

# ===== 方差分析执行 =====
results = []
for var in variables:
    try:
        # 数据清洗
        temp_df = df[[var, 'exam_score']].dropna()
      
        # 分组检查（至少2组）
        groups = temp_df.groupby(var)['exam_score']
        group_data = [group for _, group in groups]
        if len(group_data) < 2:
            print(f"变量 {var} 分组不足，已跳过")
            continue
          
        # 方差分析
        f_stat, p_value = stats.f_oneway(*group_data)
      
        # 计算效应量η²
        grand_mean = temp_df['exam_score'].mean()
        ss_between = sum([len(g)*(np.mean(g)-grand_mean)**2 for g in group_data])
        ss_total = np.var(temp_df['exam_score'], ddof=1) * (len(temp_df)-1)
        eta_sq = ss_between / ss_total if ss_total != 0 else 0
      
        # 结论判断
        conclusion = '与成绩不独立' if p_value < alpha else '与成绩独立'
      
        # 存储结果
        results.append({
            '变量': var,
            'F值': f_stat,
            'p值': p_value,
            '效应量η²': eta_sq,
            '结论': conclusion  # 修改后的结论字段
        })
      
    except Exception as e:
        print(f"变量 {var} 分析失败: {str(e)}")
        continue

# ===== 结果处理与展示 =====
# 转换为DataFrame
results_df = pd.DataFrame(results)
results_df['F值'] = results_df['F值'].round(2)
results_df['p值'] = results_df['p值'].round(4)
results_df['效应量η²'] = results_df['效应量η²'].round(3)

# 定义颜色高亮函数
def highlight_conclusion(row):
    color = 'red' if row['结论'] == '与成绩不独立' else 'black'
    return [f'color: {color}' for _ in row]

# 生成样式表格
styled_table = results_df.style\
    .apply(highlight_conclusion, axis=1)\
    .hide(axis="index")\
    .set_caption(f"变量对成绩的影响分析 (α={alpha})")\
    .format({
        'F值': "{:.2f}",
        'p值': "{:.4f}",
        '效应量η²': "{:.3f}"
    })

# 在Jupyter中直接显示（不要用print）
styled_table

# --------------------------------------------------------------------
# 【第 59 段 / 共 62 段】
# --------------------------------------------------------------------


# 定义所有分析变量
variables = [
    'gender',               # 性别
    'study_hours_group',    # 学习时长分组
    'social_hours_group',   # 社交使用分组
    'part_time_job_cn',     # 兼职
    'attendance_group',     # 出勤率分组
    'sleep_group',          # 睡眠时长分组
    'diet_quality_cn',      # 饮食质量
    'parental_education_cn',# 家长教育水平
    'extracurricular_cn',   # 课外活动参与
    'internet_quality_cn',  # 网络质量
    'exercise_group',       # 锻炼频率
    'mental_health_group'   # 心理健康
]

# 设置统一风格
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 逐个生成独立图表
for var in variables:
    # 创建交叉表
    ct = pd.crosstab(
        df['score_group'],  # 行：成绩分组
        df[var],            # 列：分析变量
        normalize='columns'
    )
  
    # 创建大尺寸画布（宽度适应变量类别数量）
    plt.figure(figsize=(max(8, len(ct.columns)*1.5), 6))  # 动态调整宽度
  
    # 绘制热力图
    ax = sns.heatmap(
        ct,
        annot=True,
        fmt='.1%',
        cmap='Blues',
        linewidths=0.5,
        annot_kws={'size': 12}
    )
  
    # 优化标签
    plt.title(f"变量: {var} → 成绩分布", fontsize=14)
    plt.xlabel(var, fontsize=12)
    plt.ylabel("成绩分组", fontsize=12)
    plt.xticks(rotation=30, ha='right', fontsize=10)  # 标签右对齐倾斜30度
    plt.yticks(rotation=0, fontsize=10)
  
    # 显示当前图后暂停，按任意键继续
    plt.tight_layout()
    plt.show()

# --------------------------------------------------------------------
# 【第 60 段 / 共 62 段】
# --------------------------------------------------------------------
from numpy.linalg import svd
class CA(object): #对应分析函数
    """Simple corresondence analysis.
    
    Inputs
    ------
    ct : array_like
      Two-way contingency table. If `ct` is a pandas DataFrame object,
      the index and column values are used for plotting.
    Notes
    -----
    The implementation follows that presented in 'Correspondence
    Analysis in R, with Two- and Three-dimensional Graphics: The ca
    Package,' Journal of Statistical Software, May 2007, Volume 20,
    Issue 3.
    """

    def __init__(self, ct):
        self.rows = ct.index.values if hasattr(ct, 'index') else None
        self.cols = ct.columns.values if hasattr(ct, 'columns') else None
        
        # contingency table
        N = np.matrix(ct, dtype=float)

        # correspondence matrix from contingency table
        P = N / N.sum()

        # row and column marginal totals of P as vectors
        r = P.sum(axis=1)
        c = P.sum(axis=0).T

        # diagonal matrices of row/column sums
        D_r_rsq = np.diag(1. / np.sqrt(r.A1))
        D_c_rsq = np.diag(1. / np.sqrt(c.A1))

        # the matrix of standarized residuals
        S = D_r_rsq * (P - r * c.T) * D_c_rsq

        # compute the SVD
        U, D_a, V = svd(S, full_matrices=False)
        D_a = np.asmatrix(np.diag(D_a))
        V = V.T

        # principal coordinates of rows
        F = D_r_rsq * U * D_a
        

        # principal coordinates of columns
        G = D_c_rsq * V * D_a
        

        # standard coordinates of rows
        X = D_r_rsq * U

        # standard coordinates of columns
        Y = D_c_rsq * V

        # the total variance of the data matrix
        inertia = sum([(P[i,j] - r[i,0] * c[j,0])**2 / (r[i,0] * c[j,0])
                       for i in range(N.shape[0])
                       for j in range(N.shape[1])])

        self.F = F.A
        self.G = G.A
        self.X = X.A
        self.Y = Y.A
        self.inertia = inertia
        self.eigenvals = np.diag(D_a)**2

    def plot(self):
        """Plot the first and second dimensions."""
        xmin, xmax = None, None
        ymin, ymax = None, None
        if self.rows is not None:
            for i, t in enumerate(self.rows):
                x, y = self.F[i,0], self.F[i,1]
                plt.text(x, y, t, va='center', ha='center', color='r',fontsize=5)
                xmin = min(x, xmin if xmin else x)
                xmax = max(x, xmax if xmax else x)
                ymin = min(y, ymin if ymin else y)
                ymax = max(y, ymax if ymax else y)
        else:
            plt.plot(self.F[:, 0], self.F[:, 1], 'ro')

        if self.cols is not None:
            for i, t in enumerate(self.cols):
                x, y = self.G[i,0], self.G[i,1]
                plt.text(x, y, t, va='center', ha='center', color='b',fontsize=5)
                xmin = min(x, xmin if xmin else x)
                xmax = max(x, xmax if xmax else x)
                ymin = min(y, ymin if ymin else y)
                ymax = max(y, ymax if ymax else y)
        else:
            plt.plot(self.G[:, 0], self.G[:, 1], 'bs')

        if xmin and xmax:
            pad = (xmax - xmin) * 0.1
            plt.xlim(xmin - pad, xmax + pad)
        if ymin and ymax:
            pad = (ymax - ymin) * 0.1
            plt.ylim(ymin - pad, ymax + pad)

        plt.grid()
        plt.xlabel('Dim 1')
        plt.ylabel('Dim 2')

    def scree_diagram(self, perc=True, *args, **kwargs):
        """Plot the scree diagram."""
        eigenvals = self.eigenvals
        xs = np.arange(1, eigenvals.size + 1, 1)
        ys = 100. * eigenvals / eigenvals.sum() if perc else eigenvals
        plt.plot(xs, ys, *args, **kwargs)
        plt.xlabel('Dimension')
        plt.ylabel('Eigenvalue' + (' [%]' if perc else ''))

# --------------------------------------------------------------------
# 【第 61 段 / 共 62 段】
# --------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# 定义分析变量列表
variables = [
    'gender', 'study_hours_group', 'social_hours_group',
    'part_time_job_cn', 'attendance_group', 'sleep_group',
    'diet_quality_cn', 'parental_education_cn', 'extracurricular_cn',
    'internet_quality_cn', 'exercise_group', 'mental_health_group'
]

# 设置图形参数
FIG_WIDTH = 8   # 单图宽度
FIG_HEIGHT = 6  # 单图高度
DPI = 150       # 分辨率

# 遍历每个变量单独生成图形
for var in variables:
    # 创建独立画布
    plt.figure(figsize=(FIG_WIDTH, FIG_HEIGHT), dpi=DPI)
  
    # 生成列联表
    cross_tab = pd.crosstab(df[var], df['score_group'])
  
    try:
        # 执行对应分析
        ca = CA(cross_tab)
        ca.plot()
        plt.title(f"{var} vs 成绩", fontsize=12, pad=20)
      
        # 调整边距
        plt.subplots_adjust(left=0.15, right=0.85, top=0.85, bottom=0.15)
      
    except Exception as e:
        print(f"变量 {var} 分析失败: {str(e)}")
        plt.close()
        continue
  
    # 显示当前图形
    plt.show()

# --------------------------------------------------------------------
# 【第 62 段 / 共 62 段】
# --------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 定义分析变量
variables = [
    ('study_hours_per_day', '每日学习时长（小时）'), 
    ('social_media_hours', '社交媒体使用时长（小时）'),
    ('sleep_hours', '睡眠时长（小时）'),
    ('diet_quality', '饮食质量（1-3分）'), 
    ('exercise_frequency', '锻炼频率（次/周）'),
    ('internet_quality', '网络质量（1-3分）'),
    ('mental_health_rating', '心理健康评分（1-10分）')
]

# 设置画布
plt.figure(figsize=(15, 20))

# 遍历每个变量
for i, (var, label) in enumerate(variables, 1):
    # 创建子图
    ax = plt.subplot(4, 2, i)
  
    # 数据清洗与验证
    temp_df = df[[var, 'exam_score']].dropna()
  
    # 关键验证步骤
    if len(temp_df) < 2:
        plt.text(0.5, 0.5, 
                f"有效数据不足 (n={len(temp_df)})",
                ha='center', va='center', 
                transform=ax.transAxes,
                color='red')
        plt.title(f"{label} (数据不足)", fontsize=12)
        plt.axis('off')
        continue
  
    try:
        # 绘制散点图与回归线
        sns.regplot(
            x=var, 
            y='exam_score', 
            data=temp_df,
            scatter_kws={'alpha': 0.4, 'color': '#1f77b4'},
            line_kws={'color': '#d62728', 'lw': 2},
            ci=95
        )
      
        # 计算统计指标
        r, p = stats.pearsonr(temp_df[var], temp_df['exam_score'])
        n = len(temp_df)
      
        # 添加统计标注
        text = f'r = {r:.2f}\np = {p:.2e}\nn = {n}'
        ax.text(
            0.05, 0.92, 
            text,
            transform=ax.transAxes,
            fontsize=12,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray')
        )
      
        # 图表美化
        plt.title(f"{label} vs 成绩", fontsize=14, pad=15)
        plt.xlabel(label, fontsize=12)
        plt.ylabel("考试成绩", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.3)
  
    except Exception as e:
        plt.text(0.5, 0.5, 
                f"分析失败: {str(e)}",
                ha='center', va='center', 
                transform=ax.transAxes,
                color='red')
        plt.title(f"{label} (分析错误)", fontsize=12)
        plt.axis('off')

plt.tight_layout(pad=3.0)
plt.show()
