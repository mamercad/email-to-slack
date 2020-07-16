#!/usr/bin/env python3

import email, requests, sys

slack = 'https://hooks.slack.com/services/...'
channel = '#...'
username = '...'

lines = b""
for line in sys.stdin:
  lines += str.encode(line)
msg = email.message_from_bytes(lines)
message = msg.get_payload()

headers={'Content-Type': 'application/json'}

payload = {
  'channel': channel,
  'username': username,
  'text': message,
}

try:
  r = requests.post(slack, headers=headers, json=payload)
  print(r.status_code, r.text)
except Exception as e:
  print(e)
