# Databricks / PySpark Data Ingestion

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ECommerceAnalytics").getOrCreate()

# Load CSV files
customers_df = spark.read.csv("/FileStore/data/customers.csv", header=True, inferSchema=True)
merchants_df = spark.read.csv("/FileStore/data/merchants.csv", header=True, inferSchema=True)
products_df = spark.read.csv("/FileStore/data/products.csv", header=True, inferSchema=True)
sessions_df = spark.read.csv("/FileStore/data/sessions.csv", header=True, inferSchema=True)
transactions_df = spark.read.csv("/FileStore/data/transactions.csv", header=True, inferSchema=True)

# Create temp views
customers_df.createOrReplaceTempView("customers")
merchants_df.createOrReplaceTempView("merchants")
products_df.createOrReplaceTempView("products")
sessions_df.createOrReplaceTempView("sessions")
transactions_df.createOrReplaceTempView("transactions")

print("Data ingestion completed successfully.")
