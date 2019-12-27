[
    {
        "id": "4ec50db1.fe48e4",
        "type": "tab",
        "label": "Flow 2",
        "disabled": false,
        "info": ""
    },
    {
        "id": "fb901275.46f14",
        "type": "inject",
        "z": "4ec50db1.fe48e4",
        "name": "",
        "topic": "",
        "payload": ",,25.5",
        "payloadType": "str",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 130.5,
        "y": 90,
        "wires": [
            [
                "20161f87.1dbc3"
            ]
        ]
    },
    {
        "id": "20161f87.1dbc3",
        "type": "mqtt out",
        "z": "4ec50db1.fe48e4",
        "name": "",
        "topic": "mcs/D4mYU05y/WqLLSs50YAevSc3I/Temperature",
        "qos": "2",
        "retain": "",
        "broker": "6ef3f07f.69b62",
        "x": 510.5,
        "y": 237,
        "wires": []
    },
    {
        "id": "d221a1bf.13d18",
        "type": "inject",
        "z": "4ec50db1.fe48e4",
        "name": "",
        "topic": "",
        "payload": ",,30.5",
        "payloadType": "str",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 142,
        "y": 372,
        "wires": [
            [
                "20161f87.1dbc3"
            ]
        ]
    },
    {
        "id": "6ef3f07f.69b62",
        "type": "mqtt-broker",
        "z": "",
        "name": "MCS Cloud",
        "broker": "mqtt.mcs.mediatek.com",
        "port": "1883",
        "clientid": "",
        "usetls": false,
        "compatmode": true,
        "keepalive": "60",
        "cleansession": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "closeTopic": "",
        "closeQos": "0",
        "closePayload": "",
        "willTopic": "",
        "willQos": "0",
        "willPayload": ""
    }
]
