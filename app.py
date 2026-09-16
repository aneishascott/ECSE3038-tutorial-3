from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall", "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

def list_devices(devices):
    for device in devices:
        print(device["name"] + "," + str(device["temp"]))
list_devices(readings)

def average_temp(devices):
    total_temp = sum(device['temp'] for device in devices)
    return total_temp / len(devices) if devices else 0
print(f"Average Temperature: {average_temp(readings):.15f}")

def hottest_devices(devices):
    max_temp = devices[0]['temp']
    for i in range(len(devices)):
        if devices[i]['temp']>max_temp:
            max_temp = devices[i]['temp']
    hottest_device = next(device for device in devices if device['temp'] == max_temp)
    return hottest_device
print(hottest_devices(readings))

@app.get("/readings")
async def get_readings():
    return readings

@app.get("/readings/hottest")
async def get_hottest_reading():
    hottest_device = hottest_devices(readings)
    return hottest_device