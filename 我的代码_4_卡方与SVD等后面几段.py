# ======================================================================
# ④ 后面的卡方检验、SVD 等几段（可选读）
# 来源：student-habits-vs-academic-performance-ml-90.ipynb
# ======================================================================

> 这些是 notebook 最后几段，跟今天的任务无关，先别管。


# --------------------------------------------------------------------
# 【第 1 段 / 共 7 段】
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
# 【第 2 段 / 共 7 段】
# --------------------------------------------------------------------
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns
import scipy 
import pandas as pd
from collections import Counter

# --------------------------------------------------------------------
# 【第 3 段 / 共 7 段】
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
# 【第 4 段 / 共 7 段】
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
# 【第 5 段 / 共 7 段】
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
# 【第 6 段 / 共 7 段】
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
# 【第 7 段 / 共 7 段】
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
