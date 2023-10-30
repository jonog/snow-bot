from helpers import snowflake

def run_sql(q):
    ctx = snowflake.snowflake_connection()
    records = snowflake.raw_query(ctx, q)
    return records
