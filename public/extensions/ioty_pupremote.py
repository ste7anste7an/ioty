from ioty.pupremote import  PUPRemoteSensor, SPIKE_ULTRASONIC

_pupsensor = None

def init(sensor_id=SPIKE_ULTRASONIC):
    global _pupsensor
    _pupsensor = PUPRemoteSensor(sensor_id=SPIKE_ULTRASONIC)

def add_command(pup_function,to_hub_fmt="",from_hub_fmt=""):
    _pupsensor.add_command(pup_function,to_hub_fmt,from_hub_fmt)

def process():
    _pupsensor.process()