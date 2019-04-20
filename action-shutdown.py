#!/usr/bin/env python2
# -*-: coding utf-8 -*-

from hermes_python.hermes import Hermes
import hermes_python
import os

if __name__ == "__main__":

    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, res.decode("utf-8"))

    os.system('sudo shutdown now -h')
