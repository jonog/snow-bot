import logging
import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from helpers import slack

import subscription_metrics.formatter
import subscription_metrics.queries

import sql_run.modal
import sql_run.query
import sql_run.result_processor

logging.basicConfig(level=logging.DEBUG)

# Load credentials
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]


# Initialise the Slack Bolt app
app = App(token=SLACK_BOT_TOKEN)



# Process Events for Subscription Metrics Feature

@app.event("app_mention")
def event_test(event, say):
    records = subscription_metrics.queries.get_daily_subscriber_data()
    subscriber_count = records[0]['SUBSCRIBER_COUNT']
    previous_subscriber_count = records[1]['SUBSCRIBER_COUNT']
    growth = 100.0 * (subscriber_count - previous_subscriber_count) / (previous_subscriber_count * 1.0)
    say(blocks=subscription_metrics.formatter.format_blocks(subscriber_count, growth))



# Process Events for SQL Run Feature

app.shortcut("snowy_sql_run")(ack=slack.ack_shortcut, lazy=[sql_run.modal.modal])

@app.view("snowy_sql_run")
def submission(ack, body, client, view, logger):
    ack()
    query = sql_run.modal.parse_query_from_view(view)
    results = sql_run.query.run_sql(query)
    sql_run.result_processor.process(client, body["user"]["id"], results)



# Start Websockets App

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
