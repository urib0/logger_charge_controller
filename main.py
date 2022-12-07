#!/usr/bin/env python3
import json
from epevermodbus.driver import EpeverChargeController
import pprint

# 設定値読み込み
with open("./config.json", "r") as f:
    conf = json.loads(f.read())

port = conf["serial_port"]
slaveaddr = 1

controller = EpeverChargeController(port,slaveaddr)
d = {
    "solar_v":controller.get_solar_voltage(),
    "solar_i":controller.get_solar_current(),
    "solar_w":controller.get_solar_power(),
    "battery_v":controller.get_battery_voltage(),
    "battery_i":controller.get_battery_current(),
    "battery_w":controller.get_battery_power()
}

pprint.pprint(d)