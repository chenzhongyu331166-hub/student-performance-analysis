# ======================================================================
# ③ 相关性/分箱相关细节（要一起看 2 才好懂）
# 来源：student-habits-vs-academic-performance-ml-90.ipynb
# ======================================================================

> 主要是 pd.cut 分箱 + 每列 unique() 探查，属于画图前的准备。


# --------------------------------------------------------------------
# 【第 1 段 / 共 35 段】
# --------------------------------------------------------------------
df['study_hours_per_day'].unique()

# --------------------------------------------------------------------
# 【第 2 段 / 共 35 段】
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
# 【第 3 段 / 共 35 段】
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
# 【第 4 段 / 共 35 段】
# --------------------------------------------------------------------
df['social_media_hours'].unique()

# --------------------------------------------------------------------
# 【第 5 段 / 共 35 段】
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
# 【第 6 段 / 共 35 段】
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
# 【第 7 段 / 共 35 段】
# --------------------------------------------------------------------
df['netflix_hours'].unique()

# --------------------------------------------------------------------
# 【第 8 段 / 共 35 段】
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
# 【第 9 段 / 共 35 段】
# --------------------------------------------------------------------
df['part_time_job'].unique()

# --------------------------------------------------------------------
# 【第 10 段 / 共 35 段】
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
# 【第 11 段 / 共 35 段】
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
# 【第 12 段 / 共 35 段】
# --------------------------------------------------------------------
df['attendance_percentage'].unique()

# --------------------------------------------------------------------
# 【第 13 段 / 共 35 段】
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
# 【第 14 段 / 共 35 段】
# --------------------------------------------------------------------
df['sleep_hours'].unique()

# --------------------------------------------------------------------
# 【第 15 段 / 共 35 段】
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
# 【第 16 段 / 共 35 段】
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
# 【第 17 段 / 共 35 段】
# --------------------------------------------------------------------
df['diet_quality'].unique()

# --------------------------------------------------------------------
# 【第 18 段 / 共 35 段】
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
# 【第 19 段 / 共 35 段】
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
# 【第 20 段 / 共 35 段】
# --------------------------------------------------------------------
df['exercise_frequency'].unique()

# --------------------------------------------------------------------
# 【第 21 段 / 共 35 段】
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
# 【第 22 段 / 共 35 段】
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
# 【第 23 段 / 共 35 段】
# --------------------------------------------------------------------
df['parental_education_level'].unique()

# --------------------------------------------------------------------
# 【第 24 段 / 共 35 段】
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
# 【第 25 段 / 共 35 段】
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
# 【第 26 段 / 共 35 段】
# --------------------------------------------------------------------
df['internet_quality'].unique()

# --------------------------------------------------------------------
# 【第 27 段 / 共 35 段】
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
# 【第 28 段 / 共 35 段】
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
# 【第 29 段 / 共 35 段】
# --------------------------------------------------------------------
df['mental_health_rating'].unique()

# --------------------------------------------------------------------
# 【第 30 段 / 共 35 段】
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
# 【第 31 段 / 共 35 段】
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
# 【第 32 段 / 共 35 段】
# --------------------------------------------------------------------
df['extracurricular_participation'].unique()

# --------------------------------------------------------------------
# 【第 33 段 / 共 35 段】
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
# 【第 34 段 / 共 35 段】
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
# 【第 35 段 / 共 35 段】
# --------------------------------------------------------------------
df['exam_score'].unique()
