from pyspark.sql.functions import lit

# Funnel conversion percentages
total_sessions = sessions_df.count()
add_to_cart_count = sessions_df.filter(col("add_to_cart") == "Yes").count()
checkout_count = sessions_df.filter(col("checkout_initiated") == "Yes").count()
orders_count = transactions_df.count()

funnel_data = [
    ("Sessions", total_sessions, 100),
    ("Add To Cart", add_to_cart_count, (add_to_cart_count / total_sessions) * 100),
    ("Checkout", checkout_count, (checkout_count / total_sessions) * 100),
    ("Orders", orders_count, (orders_count / total_sessions) * 100)
]

funnel_df = spark.createDataFrame(funnel_data, ["Stage", "Users", "ConversionPercent"])

funnel_df.show()

# Save funnel analysis
funnel_df.write.mode("overwrite").parquet("/FileStore/gold/funnel_metrics")
