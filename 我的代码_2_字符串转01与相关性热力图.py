# ======================================================================
# ② 把字符串列换成 0/1，算相关系数矩阵，画热力图
# 来源：student-habits-vs-academic-performance-ml-90.ipynb
# ======================================================================

> 她记得的关键操作都在这里：get_dummies(0/1)、corr()、np.triu 做遮罩、heatmap。


# --------------------------------------------------------------------
# 【第 1 段 / 共 7 段】
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
# 【第 2 段 / 共 7 段】
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
# 【第 3 段 / 共 7 段】
# --------------------------------------------------------------------

# 复制数据（根据实际列名调整）
num_df = df.copy()

# 删除非数值型或不需要的列
num_df.drop(['age', 'student_id', ], axis=1, inplace=True)

num_df.head()

# --------------------------------------------------------------------
# 【第 4 段 / 共 7 段】
# --------------------------------------------------------------------
corrMatrix = num_df.select_dtypes(include=[np.number]).corr() #相关系数矩阵
corrMatrix

# --------------------------------------------------------------------
# 【第 5 段 / 共 7 段】
# --------------------------------------------------------------------
fig = plt.figure(dpi=100,figsize=[9,8])
sns.heatmap(corrMatrix, annot=True,fmt='.2f')#,cmap='Reds'
plt.show()

# --------------------------------------------------------------------
# 【第 6 段 / 共 7 段】
# --------------------------------------------------------------------
mask = np.triu(corrMatrix.corr()) # 新建一个mask,  np.triu() returns the lower triangle of any matrix

fig = plt.figure(dpi=100,figsize=[9,8])
sns.heatmap(corrMatrix, annot=True, mask=mask)
plt.show()

# --------------------------------------------------------------------
# 【第 7 段 / 共 7 段】
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
