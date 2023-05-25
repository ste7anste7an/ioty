from machine import Pin
from time import sleep_ms

def main():
    led = Pin(2, Pin.OUT)
    btn = Pin(0, Pin.IN, Pin.PULL_UP)

    def start_mqtt():
        from ioty.mqtt import MQTT_Service

        mqtt = MQTT_Service()
        if not mqtt.read_config():
            return

        led.off()
        mqtt.connect_wifi()
        while not mqtt.wifi_isconnected():
            for _ in range(2):
                led.on()
                sleep_ms(50)
                led.off()
                sleep_ms(50)
            sleep_ms(500)
        led.off()

        mqtt.connect_mqtt()
        led.on()
        return mqtt

    def start_mqtt_ble_mode():
        from ioty.ble import BLE_Service

        BLE_Service()
        mqtt = start_mqtt()

        while True:
            if mqtt:
                mqtt.check_msg()
            sleep_ms(10)

    def start_ap_mode():
        from ioty.http import HTTP_Service

        while True:
            led.off()
            sleep_ms(50)
            led.on()
            sleep_ms(50)
            if btn.value() == 1:
                break
        http = HTTP_Service()
        while True:
            http.wait_for_connection()
            for _ in range(2):
                led.off()
                sleep_ms(50)
                led.on()
                sleep_ms(50)

    for _ in range(3):
        led.on()
        sleep_ms(200)
        led.off()
        sleep_ms(200)

    if btn.value() == 0:
        led.on()

        ble_mode = False
        for _ in range(200):
            sleep_ms(10)
            if btn.value() == 1:
                ble_mode = True
                break

        if ble_mode:
            start_mqtt_ble_mode()
        else:
            start_ap_mode()

main()