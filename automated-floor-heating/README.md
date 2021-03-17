Automated floor heating
=======================

Introduction:
-------------
A automated home heating system will only work properly if all heated elements are automated. I started to use TADO in my home and soon discovered that I had to include the floor heating into the system. The floor heating in my home includes the down stair kitchen and the living area. The temperature in these areas could not kept steady because of the uncontrolled floor heating outside of TADO. How to include the floor heating into my TADO system? 

Requirements:
-------------
* Cheap.
* Integration with TADO (via Node-RED) possible.
* Connected to my home MQTT automation bus.
* Able to individually control each of the three floor heating circuits.
* The system must default to "open". If the home automation system is down the valves should be open to make heating "no matter what" possible.

My fist impression of such a system was that it would be difficult to build, that thought made me investigate ready available commercial products. I discovered quickly that the first requirement "cheap" could not be met (and that most products are proprietary and closed which makes integration difficult). The solution described in this article is surprisingly simple, cheap and can easily be integrated into any system. 

Plumbing:
---------
the most difficult part (at least for me) was to upgrade the current floor heating system to something that can be automated. The figure shows the system before the upgrade.

![automated-floor-heating-old-situation](images/automated-floor-heating-old-situation.png?raw=true)

Also I needed some motorized valves to control the three floor heating circuits. After some research I found this system on Amazon:

![Alpha-5-valve-floor-heating-24v-AC-DC-type-NO-Nomally-Opened-VA80](images/Alpha-5-valve-floor-heating-24v-AC-DC-type-NO-Nomally-Opened-VA80.png?raw=true)

These  "motorized knobs" are used to open and close a "thermostatic valve". These knobs work with a resin core that is heated by a resistor. The heated resin expands (if a current flows through it) and generates a linear motion. This motion can be used to open or close a "thermostatic valve". The linear motion can be controlled by the amount of current you sent trough the knob. This can be controlled by a PWM signal. The knobs I used are normally open (fail to open requirement), 24V and require only a few mA. The maximum power usage I saw was never more than 70mA. Full specification: `Alpha 5 valve floor heating 24v AC/DC type NO Normally Opened VA80`

These knobs can't be fitted to the current system. I had to buy and mount compatible "thermostatic valves", these are shown in the picture below:


![floor-heating-thermostat-valve](images/floor-heating-thermostat-valve.png?raw=true)

Note that next to the valve I installed looking glasses. These allow you to see the the amount of water flowing through each circuit. These have to be proven extremely useful and a absolute must when fine-tuning the system (otherwise you will have no idea what is going on).

The next figure shows the upgraded system:

![automated-floor-heating](images/automated-floor-heating.png?raw=true)

You can see the installed thermostatic valves, looking glass, valve motors and also a new pump. This pump is not only cheaper to operate (15 Watts instead of 100 Watts). It also regulates the required water pressure to the floor heating system dynamically (the demand constantly changes due to opening and closing valves). It will also minimize the pressure when all valves are closed. Something you have to take in account.... Anyhow I optimized this a bit more by turning the pump completely off if there is no demand. A Sonoff TH16 takes care of the pump. This also allows me to automatically "flush" the floor heating system if it wasn't used for some time (during the summer period).

Electronics:
------------
With the plumbing done we can dive into the electronics, The next figure shows the inside of the control system:

![automated-floor-heating-open-box](images/automated-floor-heating-open-box.png?raw=true)
![automated-floor-heating-scematic](images/automated-floor-heating-scematic.png?raw=true)

As you can see there is not much to it: A 24V power supply, a ESP32, a buck converter to step down the 24V to 5V required for the ESP32 and three MOSFET drivers to convert the 3.3V ESP PWM steering signals to 24V. 

![esp-wroom-32](images/esp-wroom-32.png?raw=true)
![irf520-mosfet-driver-module](images/irf520-mosfet-driver-module.png?raw=true)
![RS-25-24-mean-well](images/RS-25-24-mean-well.png?raw=true)

From left to right:

1. ESP-32-VROOM (Any ESP will do)
2. IRF520 MOSFET driver module
3. RS-25-24 Mean Well power supply


Software:
---------





Total costs:
------------





