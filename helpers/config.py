import os

def get_snowflake_config():
  return {
    "account": _get_env_or_raise("SNOWFLAKE_ACCOUNT"),
    "user": _get_env_or_raise("SNOWFLAKE_USER"),
    "password": _get_env_or_raise("SNOWFLAKE_PASSWORD"),
    "role": "ACCOUNTADMIN",
    "warehouse": "ANALYTICS_WH",
    "database": "ANALYTICS",
    "schema": "PUBLIC"
  }

def _get_env_or_raise(envvar):
  result = os.getenv(envvar)
  if result:
    return result
  raise Exception(f"Missing env var {envvar}")
