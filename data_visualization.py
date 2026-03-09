import pandas as pd
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# ==========================
# PLUS会员增长流失趋势图（旋转标签完美生效版）
# ==========================
def plot_plus_member_trend(df):
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    df['net_growth'] = df['new_users'] - df['expired_users']

    fig, ax1 = plt.subplots(figsize=(14, 7))

    # 左轴：新增、流失、净增长
    ax1.bar(df['month'], df['new_users'], color='#4285F4', alpha=0.7, width=15, label='当月开通数')
    ax1.bar(df['month'], -df['expired_users'], color='#EA4335', alpha=0.7, width=15, label='当月过期数')
    ax1.plot(df['month'], df['net_growth'], color='#FBBF24', linewidth=3, marker='o', label='净增长')

    ax1.set_xlabel('月份', fontsize=12)
    ax1.set_ylabel('新增 / 流失 / 净增长', fontsize=12)
    ax1.legend(loc='upper left')
    ax1.grid(alpha=0.3)

    # 右轴：生效会员数
    ax2 = ax1.twinx()
    ax2.plot(df['month'], df['active_users'], color='#10B981', linewidth=4, marker='o', label='当月生效会员数')
    ax2.set_ylabel('当月生效会员总数', fontsize=12)
    ax2.legend(loc='upper right')

    # ====================== ✅ 这里修复：旋转 100% 生效 ======================
    ax1.tick_params(axis='x', rotation=60, labelsize=10)  # 对ax1旋转，必生效！

    plt.title('商城PLUS会员增长、流失与存量趋势', fontsize=16)
    plt.tight_layout()
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    df = pd.read_excel('data_test.xlsx')
    plot_plus_member_trend(df)
