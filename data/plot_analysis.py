# plot_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

if platform.system() == "Darwin":
    # 简易设置以让matplotlib能显示中文
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
elif platform.system() == "Windows":
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 简易设置以让matplotlib能显示中文
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
else:
    pass

# ==========【衔接：读取handle输出好的清洗文件】==========
df = pd.read_csv(r"D:\我的作品\D12-pandas读筛排存\data\df_cleaned.csv", encoding="utf-8-sig")
print("✅成功读取清洗完毕数据集，行列大小：", df.shape)


print("\n==========【图1】计数条形图：考试成绩分组分布 ==========")
# ======================图1：计数条形图 countplot（分组人数分布）======================
plt.figure(figsize=(8,5))
sns.countplot(
    x="score_group",
    data=df,
    order=["不及格","及格","中等","良好","优秀"]
)
plt.title("考试成绩分组分布")
plt.xlabel("成绩组别")
plt.ylabel("学生人数")
plt.tight_layout()
plt.show(block=False) # 不阻塞，不会卡住！！
print("👉已绘制完成：考试成绩分组分布条形图")


print("\n==========【图2】数值变量相关系数热力图 ==========")
# ======================图2：数值变量相关系数热力图======================
# select_dtypes：只挑数字列做相关系数
num_df = df.select_dtypes(include=[float, int])
corr_matrix = num_df.corr()
print("----输出相关系数矩阵预览----")
print(corr_matrix.head())

plt.figure(figsize=(9,8), dpi=100)
# mask上三角，只保留下三角，图表更干净
mask = np.triu(corr_matrix)
sns.heatmap(corr_matrix, annot=True, fmt=".2f", mask=mask)
plt.title("数值变量相关系数热力图")
plt.tight_layout()
plt.show(block=False) # 不阻塞，不会卡住！！
print("👉已绘制完成：数值变量相关系数热力图")


print("\n==========【图3】交叉表热力图：学习时长分组 vs 成绩分组 ==========")
# ======================图3：交叉表热力图【分类变量 vs 成绩分组】======================
# 示例：学习时长分组 和 成绩分组 的交叉统计
ct = pd.crosstab(df["study_hours_group"], df["score_group"], normalize="columns")
print("----输出交叉占比表预览----")
print(ct)

plt.figure(figsize=(8,6))
sns.heatmap(ct, annot=True, fmt=".1%", cmap="Blues")
plt.title("学习时长分组 vs 成绩分组(占比)")
plt.tight_layout()
plt.show(block=False) # 不阻塞，不会卡住！！
print("👉已绘制完成：学习时长分组与成绩分组交叉热力图")


print("\n==========【图4】散点回归线：每日学习时长 vs 考试分数 ==========")
# ======================图4：散点+回归线：每日学习时长 vs 考试分数======================
plt.figure(figsize=(7,5))
sns.regplot(
    x="study_hours_per_day",
    y="exam_score",
    data=df,
    scatter_kws={"alpha":0.4},
    line_kws={"color":"red"}
)
plt.title("每日学习时长 vs 考试成绩")
plt.tight_layout()
plt.show(block=False) # 不阻塞，不会卡住！！
print("👉已绘制完成：学习时长与考试成绩散点回归线")

print("\n==========【图5】箱线图：不同学习时长分组的考试分数分布 ==========")
plt.figure(figsize=(8,5))
sns.boxplot(
    data=df,
    x="study_hours_group",
    y="exam_score",
    order=["低学习时长","中学习时长","高学习时长"]
)
plt.title("不同学习时长分组的考试分数分布")
plt.xlabel("学习时长分组")
plt.ylabel("考试分数")
plt.tight_layout()
plt.show(block=False) # 不阻塞，不会卡住！！
print("👉已绘制完成：箱线图")

plt.show()

print("\n✅====全部5组核心图表绘制完毕====")