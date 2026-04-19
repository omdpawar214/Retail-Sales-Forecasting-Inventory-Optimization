from src.data_preprocessing import load_data, merge_data, clean_data
from src.feature_engineering import create_features
from src.forecasting import train_model
from src.inventory import calculate_inventory, generate_inventory_report
from src.utils import save_csv
from src.feature_engineering import create_features, add_seasonality, add_demand_variation
from src.inventory import simulate_inventory

# Step 1: Load data
train, features, stores = load_data()

# Step 2: Merge
df = merge_data(train, features, stores)

# Step 3: Clean
df = clean_data(df)

# Step 4: Feature engineering
df = create_features(df)
df = add_seasonality(df)
df = add_demand_variation(df)

# Step 5: Train model
model, predictions = train_model(df)

# Step 6: Inventory calculation
safety_stock, reorder_point = calculate_inventory(predictions)

# Step 7: Simulate inventory FIRST
inventory_report = simulate_inventory(predictions)

# Step 8: Then generate report
inventory_report = generate_inventory_report(inventory_report, reorder_point)
# Step 9: Save outputs
save_csv(predictions, "outputs/predictions.csv")
save_csv(inventory_report, "outputs/inventory_report.csv")

print("Project executed successfully!")
print(f"Safety Stock: {safety_stock}")
print(f"Reorder Point: {reorder_point}")