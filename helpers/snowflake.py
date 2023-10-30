from helpers import config

import snowflake.connector

def snowflake_connection():

  snowflake_cfg = config.get_snowflake_config()

  ctx = snowflake.connector.connect(
    user=snowflake_cfg["user"],
    password=snowflake_cfg["password"],
    role=snowflake_cfg["role"],
    account=snowflake_cfg["account"],
    warehouse=snowflake_cfg["warehouse"],
    database=snowflake_cfg["database"],
    schema=snowflake_cfg["schema"],
  )

  return ctx

# Helper Functions

def get_records(ctx, database, schema, table):
  cs = ctx.cursor(snowflake.connector.DictCursor)
  allrows_lazy = cs.execute(f"select * from {database}.{schema}.{table}")
  return allrows_lazy.fetchall()

def raw_query(ctx, query):
  cs = ctx.cursor(snowflake.connector.DictCursor)
  allrows_lazy = cs.execute(query)
  return allrows_lazy.fetchall()
