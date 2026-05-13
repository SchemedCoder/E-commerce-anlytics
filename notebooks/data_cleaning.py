from pyspark.sql.functions import col, when

# Remove duplicates
customers_clean = customers_df.dropDuplicates(["customer_id"])
sessions_clean = sessions_df.dropDuplicates(["session_id"])
transactions_clean = transactions_df.dropDuplicates(["transaction_id"])

# Handle nulls
customers_clean = customers_clean.fillna({"acquisition_channel": "Unknown"})
sessions_clean = sessions_clean.fillna({
    "add_to_cart": "No",
    "checkout_initiated": "No"
})

# Standardize Yes/No fields
sessions_clean = sessions_clean.withColumn(
    "add_to_cart_flag",
    when(col("add_to_cart") == "Yes", 1).otherwise(0)
).withColumn(
    "checkout_flag",
    when(col("checkout_initiated") == "Yes", 1).otherwise(0)
)

# Save cleaned layers
customers_clean.write.mode("overwrite").parquet("/FileStore/clean/customers")
sessions_clean.write.mode("overwrite").parquet("/FileStore/clean/sessions")
transactions_clean.write.mode("overwrite").parquet("/FileStore/clean/transactions")

print("Data cleaning completed.")
