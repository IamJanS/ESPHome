
ESPHome @Home
=============

### Listing of all ESPHome devices running in my home. 


| Name | Device | Interface | Board | Platform |
|------|--------|-----------|-------|----------|
| i031-scullery-light | Lamp | [Sonoff MINI R2](https://devices.esphome.io/devices/Sonoff-Mini-Relay) | [esp8285](https://docs.platformio.org/en/stable/boards/espressif8266/esp8285.html) | [esp8266](https://docs.platformio.org/en/stable/boards/espressif8266/espmxdevkit.html) |
| i032-bathroom-light | Lamp | [Sonoff MINI R2](https://devices.esphome.io/devices/Sonoff-Mini-Relay) | [esp8285](https://docs.platformio.org/en/stable/boards/espressif8266/esp8285.html) | [esp8266](https://docs.platformio.org/en/stable/boards/espressif8266/espmxdevkit.html) |
| i034-office-light | Lamp | [Sonoff MINI R2](https://devices.esphome.io/devices/Sonoff-Mini-Relay) | [esp8285](https://docs.platformio.org/en/stable/boards/espressif8266/esp8285.html) | [esp8266](https://docs.platformio.org/en/stable/boards/espressif8266/espmxdevkit.html) |
| i036-bathroom-fan | Ruck EM 125L EC 01 | [Sonoff MINI R2](https://devices.esphome.io/devices/Sonoff-Mini-Relay) | [esp8285](https://docs.platformio.org/en/stable/boards/espressif8266/esp8285.html) | [esp8266](https://docs.platformio.org/en/stable/boards/espressif8266/espmxdevkit.html) |
| i037-living-room-back-fan | Suedwind Ambientika Eco | [Sonoff MiniR4 Extreme](https://devices.esphome.io/devices/Sonoff-MiniR4-Extreme) | [esp32dev](https://docs.platformio.org/en/stable/boards/espressif32/esp32dev.html) | [esp32](https://docs.platformio.org/en/stable/boards/espressif32/esp32dev.html) |
| i052-toilet-fan | Ruck EM 100L E2 01 | [Sonoff MINI R2](https://devices.esphome.io/devices/Sonoff-Mini-Relay) | [esp8285](https://docs.platformio.org/en/stable/boards/espressif8266/esp8285.html) | [esp8266](https://docs.platformio.org/en/stable/boards/espressif8266/espmxdevkit.html) |
| i055-living-room-front-fan | Suedwind Ambientika Eco | [Sonoff MiniR4 Extreme](https://devices.esphome.io/devices/Sonoff-MiniR4-Extreme) | [esp32dev](https://docs.platformio.org/en/stable/boards/espressif32/esp32dev.html) | [esp32](https://docs.platformio.org/en/stable/boards/espressif32/esp32dev.html) |
| i056-office-fan | Suedwind Ambientika Eco | [Sonoff MiniR4 Extreme](https://devices.esphome.io/devices/Sonoff-MiniR4-Extreme) | [esp32dev](https://docs.platformio.org/en/stable/boards/espressif32/esp32dev.html) | [esp32](https://docs.platformio.org/en/stable/boards/espressif32/esp32dev.html) |
| i058-kitchen-counter-light | Lamp | [Sonoff MiniR4 Extreme](https://devices.esphome.io/devices/Sonoff-MiniR4-Extreme) | [esp32dev](https://docs.platformio.org/en/stable/boards/espressif32/esp32dev.html) | [esp32](https://docs.platformio.org/en/stable/boards/espressif32/esp32dev.html) |
| i060-smart-doorbell | [Smart Doorbell](https://www.zuidwijk.com/product/smart-doorbell/) | [Zuidwijk Smart Doorbell](https://github.com/zuidwijk/esphome-doorbell/blob/main/smart-doorbell2.yaml) | [esp32dev](https://docs.platformio.org/en/stable/boards/espressif32/esp32dev.html) | [esp32](https://docs.platformio.org/en/stable/boards/espressif32/esp32dev.html) |
| i061-office-ac | Mitsubishi SRK 25 ZS | [MHI-AC-Ctrl](https://github.com/ginkage/MHI-AC-Ctrl-ESPHome) | [d1_mini](https://www.wemos.cc/en/latest/d1/d1_mini.html) | [esp8266](https://docs.platformio.org/en/stable/boards/espressif8266/espmxdevkit.html) |
| i062-bedroom-middle-ac | Mitsubishi SRK 25 ZS | [MHI-AC-Ctrl](https://github.com/ginkage/MHI-AC-Ctrl-ESPHome) | [d1_mini](https://www.wemos.cc/en/latest/d1/d1_mini.html) | [esp8266](https://docs.platformio.org/en/stable/boards/espressif8266/espmxdevkit.html) |
| i063-bedroom-back-ac | Mitsubishi SRK 25 ZS | [MHI-AC-Ctrl](https://github.com/ginkage/MHI-AC-Ctrl-ESPHome) | [d1_mini](https://www.wemos.cc/en/latest/d1/d1_mini.html) | [esp8266](https://docs.platformio.org/en/stable/boards/espressif8266/espmxdevkit.html) |
| i064-landing-ac | Mitsubishi SRK 50 ZS | [MHI-AC-Ctrl](https://github.com/ginkage/MHI-AC-Ctrl-ESPHome) | [d1_mini](https://www.wemos.cc/en/latest/d1/d1_mini.html) | [esp8266](https://docs.platformio.org/en/stable/boards/espressif8266/espmxdevkit.html) |
| i065-living-room-ac | Mitsubishi SRK 35 ZSX | [MHI-AC-Ctrl](https://github.com/ginkage/MHI-AC-Ctrl-ESPHome) | [d1_mini](https://www.wemos.cc/en/latest/d1/d1_mini.html) | [esp8266](https://docs.platformio.org/en/stable/boards/espressif8266/espmxdevkit.html) |

### How I use ESPHome on my Linux workstation:

Editing with Visual Studio Code.

Build with ESPHome `esphome` docker container:
```
docker exec -it esphome esphome run i063_bedroom_back_ac.yaml
```

Build started by keyboard binding in Visual Studio Code:

```
[
    {
        "key": "ctrl+e r",
        "command": "workbench.action.terminal.sendSequence",
        "args": { "text": "docker exec -it esphome esphome run ${fileBasename}\u000D" },
        "when": "editorLangId == yaml && resourceFilename.endsWith('.yaml')"
      }
]
```