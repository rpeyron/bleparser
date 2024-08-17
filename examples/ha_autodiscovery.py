import json

def publish_ha_autodiscovery(mqtt_client, data, mac, state_topic):
    had_topic_prefix = "homeassistant/sensor/ble2mqtt/" + mac 
    had_topic_suffix = "/config"
    had_base_object = {
            "stat_t": state_topic,
            "name": mac , 
            "uniq_id": "ble2mqtt_"+mac,
            "state_class": "measurement",
            "dev": { "ids": mac.replace(":", ""), "name": mac, "sw_version": "ble2mqtt 0.1", "via_device": "ble2mqtt" },
            #"value_template": "{{ value_json.temperature }}",
            #"unit_of_measurement": "°C", 
            #"icon": "mdi:thermometer"
    }

    if ("temperature" in data):
        mqtt_client.publish(had_topic_prefix + "_temperature" + had_topic_suffix, json.dumps({**had_base_object,
            "dev_cla": "temperature", 
            "name": had_base_object["name"] + " Temperature", 
            "uniq_id": had_base_object["name"] + "_temperature",
            "val_tpl": "{{ value_json.temperature }}",
            "unit_of_meas": "°C", 
            "icon": "mdi:thermometer"
        }))
    
    if ("humidity" in data):
        mqtt_client.publish(had_topic_prefix + "_humidity" + had_topic_suffix, json.dumps({**had_base_object,
            "dev_cla": "humidity", 
            "name": had_base_object["name"] + " Humidity", 
            "uniq_id": had_base_object["name"] + "_humidity",
            "val_tpl": "{{ value_json.humidity }}",
            "unit_of_meas": "%", 
            "icon": "mdi:gauge"
        }))


