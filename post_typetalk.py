#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys

topic_id='<topic id>'
api_token='<api token>'

def main():

  lines = sys.stdin.readlines()
  for i, line in enumerate(lines):
    message = message + line

  r = requests.post('https://typetalk.com/api/v1/topics/' + topic_id +'?typetalkToken=' + api_token, {'message': message})

  r.status_code
  r.json()

if __name__ == "__main__":
  main()