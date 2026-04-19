import numpy as np

def calculate_inventory(df):
    lead_time = 7  # days
    z = 1.65  # service level

    demand = df['Predicted'].mean()
    std_dev = df['Predicted'].std()

    safety_stock = z * std_dev * np.sqrt(lead_time)
    reorder_point = (demand * lead_time) + safety_stock

    return safety_stock, reorder_point


def generate_inventory_report(df, reorder_point):
    df['Reorder'] = df['Predicted'].apply(lambda x: "YES" if x < reorder_point else "NO")
    return df

def simulate_inventory(df):
    # Assume initial stock
    df['Stock'] = df['Predicted'] * 1.5

    # Simulate stock consumption
    df['Stock'] = df['Stock'] - df['Actual']

    return df

def generate_inventory_report(df, reorder_point):
    def decision(row):
        if row['Stock'] <= 0:
            return "STOCK OUT"
        elif row['Stock'] < reorder_point:
            return "REORDER"
        elif row['Stock'] > reorder_point * 2:
            return "OVERSTOCK"
        else:
            return "OK"

    df['Inventory_Status'] = df.apply(decision, axis=1)

    return df