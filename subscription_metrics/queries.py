from helpers import snowflake

def get_daily_subscriber_data():
    ctx = snowflake.snowflake_connection()
    records = snowflake.raw_query(ctx, "select * from analytics.public.daily_subscribers order by reporting_date desc limit 2")
    return records
