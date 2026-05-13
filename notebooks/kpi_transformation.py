from pyspark.sql.functions import countDistinct, sum, avg

# Customer KPIs
customer_kpis = transactions_df.groupBy("customer_id").agg(
    countDistinct("transaction_id").alias("total_orders"),
    sum("revenue").alias("total_revenue"),
    avg("revenue").alias("avg_order_value")
)

# Merchant KPIs
merchant_kpis = transactions_df.groupBy("merchant_id").agg(
    countDistinct("transaction_id").alias("merchant_orders"),
    sum("revenue").alias("merchant_gmv")
)

# Funnel KPIs
total_sessions = sessions_df.count()
product_views = sessions_df.filter(col("product_viewed").isNotNull()).count()
add_to_cart = sessions_df.filter(col("add_to_cart") == "Yes").count()
checkout = sessions_df.filter(col("checkout_initiated") == "Yes").count()
orders = transactions_df.count()

print(f"Total Sessions: {total_sessions}")
print(f"Product Views: {product_views}")
print(f"Add to Cart: {add_to_cart}")
print(f"Checkout Initiated: {checkout}")
print(f"Orders: {orders}")

# Save KPI outputs
customer_kpis.write.mode("overwrite").parquet("/FileStore/gold/customer_kpis")
merchant_kpis.write.mode("overwrite").parquet("/FileStore/gold/merchant_kpis")
