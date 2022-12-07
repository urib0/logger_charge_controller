#!/usr/bin/env python3
import json
from epevermodbus.driver import EpeverChargeController
import os
import datetime
import time

def logging(path, name, data):
    timestamp = datetime.datetime.now()
    filename = name + "_" + timestamp.strftime("%Y-%m-%d") + ".csv"
    write_str = timestamp.strftime("%Y/%m/%d %H:%M:%S") + "," + data
    path = path + "/" + name + "/"

    os.makedirs(path, exist_ok=True)
    f = open(path + filename, mode="a")
    f.write(write_str + "\n")
    f.close()

# 設定値読み込み
with open("./config.json", "r") as f:
    conf = json.loads(f.read())

path = conf["basedir"] + "/" + conf["logdir_name"]
port = conf["serial_port"]
slaveaddr = 1

controller = EpeverChargeController(port,slaveaddr)

while True:
    data = f'\
solar_v={controller.get_solar_voltage()};\
solar_i={controller.get_solar_current()};\
solar_w={controller.get_solar_power()};\
battery_v={controller.get_battery_voltage()};\
battery_i={controller.get_battery_current()};\
battery_w={controller.get_battery_power()};\
status=0\
'

    logging(path, conf["sensor_name"], str(data))

    if not conf["interval"]:
        break
    time.sleep(conf["interval"])
