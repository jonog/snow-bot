
## Snow-bot

### Getting Started
* Setup Snowflake - see below
* Setup Slack App
* Docker is a pre-requisite
* Setup credentials in `.env` using `.env.sample`

```
docker-compose build && docker-compose up 
```

### Instructions for Setting up Slack App
* Enable Socket Mode
* Setup a Slack shortcut (with callback ID `snowy_sql_run`)
* Provide the following bot token scopes: `app_mentions:read`, `chat:write`, `commands`
* Install / re-install as required

### Instructions for Setting up Snowflake

Run the following to create the required Snowflake resources and load sample data

```sql
create or replace database analytics;

select current_database(), current_schema();

create or replace table daily_subscribers (
  reporting_date date,
  subscriber_count int
);

create or replace warehouse analytics_wh with
  warehouse_size='X-SMALL'
  auto_suspend = 180
  auto_resume = true
  initially_suspended=true;

select current_warehouse();

INSERT INTO daily_subscribers (reporting_date, subscriber_count)
VALUES ('2022-10-31', 5000);

INSERT INTO daily_subscribers (reporting_date, subscriber_count)
VALUES ('2022-11-01', 5500);

INSERT INTO daily_subscribers (reporting_date, subscriber_count)
VALUES ('2022-11-02', 6500);

select * from daily_subscribers;

```