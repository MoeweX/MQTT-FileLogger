# MQTT-FileLogger

Service to log mqtt messages to csv files.

Open TODO:
- Add transport level encryption and user authentication
- Make it possible to configure subscriptions (not all topics)

## General Idea

- The service subscribes to all topics ("#")
- Every message is logged with a timestamp in a csv file
- Every topic has its own csv file
- One csv only contains messages of a single day

## Installation/Setup

Install package:
```
git clone https://github.com/MoeweX/mqtt-filelogger.git
cd MQTT-FileLogger
python setup.py install --user
```

Run with `python mqtt-filelogger/main.py`

