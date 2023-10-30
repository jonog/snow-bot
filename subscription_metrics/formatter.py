
def add_plus(growth):
    if growth > 0:
        return "+"
    return ""

def growth_chart_emoji(growth):
    if growth > 0:
        return ":chart_with_upwards_trend:"
    if growth < 0:
        return ":chart_with_downwards_trend:"
    return ""

def headline_emoji(growth):
    if growth > 0:
        return ":fire: :fire: :fire:"
    if growth < 0:
        return ":small_red_triangle_down:"
    return ""

def format_blocks(subscriber_count, growth):
    growth_symbol = add_plus(growth)
    growth_chart = growth_chart_emoji(growth)
    headline = headline_emoji(growth)
    return [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"*Subscription Metrics* {headline}"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"*Daily subscribers {growth_chart}:* {subscriber_count} ({growth_symbol}{round(growth, 1)}%)"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Monthly churn rate :chart_with_downwards_trend::* 4.00% (-30%)"
			}
		}
    ]