#!/usr/bin/env python2
# -*-: coding utf-8 -*-

from hermes_python.hermes import Hermes
import hermes_python
import os

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def shutdown(hermes, intent_message):
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, 'Shutting down')

    os.system('sudo shutdown now -h')


if __name__ == "__main__":

    with Hermes(MQTT_ADDR.encode("ascii")) as h:
        h.subscribe_intent("Martin1887:ApagarSnips", shutdown) \
            .subscribe_intent("Martin1887:ShutdownSnips", shutdown) \
            .loop_forever()
