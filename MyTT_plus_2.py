#多謝前輩進行通達信的函數轉譯工作, 受其啓發, 我都試玩一下, 此函數純屬實驗性質, 未經驗證和DEBUG. 

#此文檔內的函數,以形態函數為主。
# COST
# WINNER

def calculate_cost(df, percentage):
    """
    Calculate the cost distribution level for a given percentage.
    :param df: DataFrame with columns ['close', 'volume']
    :param percentage: Percentage level (e.g., 85 for 85%)
    :return: Price level at which the given percentage of positions are profitable
    """
    df['value'] = df['close'] * df['volume']
    total_value = df['value'].sum()
    cumulative_value = df['value'].cumsum()
    target_value = total_value * (percentage / 100.0)
    cost_level = df[df['cumulative_value'] >= target_value].iloc[0]['close']
    return cost_level

