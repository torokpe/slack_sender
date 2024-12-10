from dotenv import load_dotenv
import os
load_dotenv()

import requests

headers = {
    'Content-type': 'application/json',
}

json_data = {
    'text': 'Hello, slack!a',
}

response = requests.post(
    fhttps://hooks.slack.com/services/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/{os.environ.get("SLACK_ID")}',
    headers=headers,
    json=json_data,
)

print(response)
