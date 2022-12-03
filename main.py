#!/usr/bin/env python3
import json

# 設定値読み込み
with open("./config.json", "r") as f:
    conf = json.loads(f.read())

print(conf)