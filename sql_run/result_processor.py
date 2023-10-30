import json

def process(client, channel, results):
    client.chat_postMessage(
        channel=channel,
        text="Here are your SQL Run results! :space_invader: ```" + str(json.dumps(results, indent=4, default=str)) + "```"
    )
