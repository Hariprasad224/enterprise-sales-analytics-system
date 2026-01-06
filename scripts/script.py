import pandas as pd
from sqlalchemy import create_engine, text
import pymysql

# -----------------------------
# 1️⃣ MySQL Connection Setup
# -----------------------------
# Replace these with your local MySQL credentials
mysql_user = 'root'
mysql_password = 'Potti2204$'
mysql_host = 'localhost'
mysql_port = 3306
mysql_db = 'enterprise_sales_analytics'

# SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}")

# -----------------------------
# 2️⃣ Load CSV into Pandas
# -----------------------------
csv_file = r"E:/Great Learning/Python/Personal/Sample - Superstore.xlsx"

# Read Excel file directly
df = pd.read_excel(csv_file, sheet_name="Orders")

# -----------------------------
# 3️⃣ Data Cleaning
# -----------------------------
# Convert dates
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce', dayfirst=True)
df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce', dayfirst=True)

# Drop rows with invalid dates
df = df.dropna(subset=['order_date', 'ship_date'])

# Reorder columns to match staging_orders table
df = df[['order_id','order_date','ship_date','customer_name','segment','state','region',
         'product_name','category','sub_category','sales','profit','discount','quantity']]

# Ensure numeric columns are correct
numeric_cols = ['sales', 'profit', 'discount', 'quantity']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# -----------------------------
# 4️⃣ Insert DataFrame into MySQL
# -----------------------------
# If table exists, append; otherwise, create it automatically
df.to_sql('staging_orders', con=engine, if_exists='append', index=False, chunksize=500)

# -----------------------------
# 5️⃣ Confirm Import
# -----------------------------
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM staging_orders"))
    count = result.fetchone()[0]
    print(f"Rows in staging_orders: {count}")


# dim_customer
dim_customer = df[['customer_name', 'segment', 'state', 'region']].drop_duplicates().reset_index(drop=True)
dim_customer['customer_id'] = dim_customer.index + 1  # surrogate key

# Reorder columns
dim_customer = dim_customer[['customer_id', 'customer_name', 'segment', 'state', 'region']]

# Insert into MySQL
dim_customer.to_sql('dim_customer', con=engine, if_exists='append', index=False)
print("dim_customer created with rows:", len(dim_customer))

# dim_product
dim_product = df[['product_name', 'category', 'sub_category']].drop_duplicates().reset_index(drop=True)
dim_product['product_id'] = dim_product.index + 1  # surrogate key

# Reorder columns
dim_product = dim_product[['product_id', 'product_name', 'category', 'sub_category']]

# Insert into MySQL
dim_product.to_sql('dim_product', con=engine, if_exists='append', index=False)
print("dim_product created with rows:", len(dim_product))

# Merge IDs from dimension tables
df_fact = df.merge(dim_customer, on='customer_name', how='left')
df_fact = df_fact.merge(dim_product, on=['product_name','category','sub_category'], how='left')

# Build fact table
fact_sales = df_fact[['order_id', 'order_date', 'ship_date', 'customer_id', 'product_id',
                      'sales', 'profit', 'discount', 'quantity']]

# Insert into MySQL
fact_sales.to_sql('fact_sales', con=engine, if_exists='append', index=False)
print("fact_sales created with rows:", len(fact_sales))


from sqlalchemy import text

with engine.connect() as conn:
    for table in ['dim_product','dim_customer','fact_sales']:
        result = conn.execute(text(f"SELECT COUNT(*) FROM {table}"))
        print(f"{table}: {result.fetchone()[0]} rows")
