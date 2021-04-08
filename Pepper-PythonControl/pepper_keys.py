#! /usr/bin/env python
# -*- encoding: UTF-8 -*-
    
laser_keys = [
    # Right X
    "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg01/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg02/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg03/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg04/X/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg05/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg06/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg07/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg08/X/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg09/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg10/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg11/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg12/X/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg13/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg14/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg15/X/Sensor/Value",
    # Right Y
    "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg01/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg02/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg03/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg04/Y/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg05/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg06/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg07/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg08/Y/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg09/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg10/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg11/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg12/Y/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg13/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg14/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg15/Y/Sensor/Value",
    # Front X
    "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg01/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg02/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg03/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg04/X/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg05/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg06/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg07/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg08/X/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg09/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg10/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg11/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg12/X/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg13/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg14/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg15/X/Sensor/Value",
    # Front Y
    "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg01/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg02/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg03/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg04/Y/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg05/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg06/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg07/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg08/Y/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg09/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg10/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg11/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg12/Y/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg13/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg14/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg15/Y/Sensor/Value",
    # Left X
    "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg01/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg02/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg03/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg04/X/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg05/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg06/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg07/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg08/X/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg09/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg10/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg11/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg12/X/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg13/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg14/X/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg15/X/Sensor/Value",
    # Left Y
    "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg01/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg02/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg03/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg04/Y/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg05/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg06/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg07/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg08/Y/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg09/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg10/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg11/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg12/Y/Sensor/Value",
    "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg13/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg14/Y/Sensor/Value", "Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg15/Y/Sensor/Value"
]