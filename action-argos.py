#!/usr/bin/env python3
# -*-: coding utf-8 -*-

from hermes_python.hermes import Hermes
import hermes_python
import os
import webbrowser

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def alarmas(hermes, intent_message):
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, 'Lanzando alarmas')
    os.system("taskkill /im chrome.exe /f")
    webbrowser.open("http://www.google.es")

def visio(hermes, intent_message):
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, 'Lanzando visio')
    os.system("taskkill /im chrome.exe /f")
    valor = intent_message.slots.instancia.first()
    if valor == "central":
        webbrowser.open("http://manten1/argos/check_mk/login.py?_origtarget=/argos/check_mk/dashboard.py?name=main&_username=argos&_password=panoptes&_login=1")
    elif valor == "delicias":
        webbrowser.open("http://del1argos/del1argos/check_mk/login.py?_origtarget=/del1argos/check_mk/dashboard.py?name=main&_username=argos&_password=panoptes&_login=1")
    elif valor == "albacete":
        webbrowser.open("http://albargos/albargos/check_mk/login.py?_origtarget=/albargos/check_mk/dashboard.py?name=main&_username=argos&_password=panoptes&_login=1")
    elif valor == "antequera":
        webbrowser.open("http://antargos/antargos/check_mk/login.py?_origtarget=/antargos/check_mk/dashboard.py?name=main&_username=argos&_password=panoptes&_login=1")
    elif valor == "alicante":
        webbrowser.open("http://www.thalesgroup.es")

if __name__ == "__main__":

    with Hermes(MQTT_ADDR.encode("ascii")) as h:
        h.subscribe_intent("jcbenayas:alarmas", alarmas) \
            .subscribe_intent("jcbenayas:visio", visio) \
            .loop_forever()