Automating all my roller shutters v0.1:
=======================================
At the time we moved into our new home I was faced with 12 manual operated roller shutters and one electrified sun screen. There was only one solution possible: electrify all of them. There are many commercial solution's. But that's not a lot of fun and these are expensive too. I decided to go completely DIY, including electronics. There are many ready available roller shutter drivers like from Shelly but its more fun to make your own PCBs.

This article is about the 0.1 version off the project. At the time of creation I was in great hurry and never tested the electronics. I designed the circuit, PCB and put the PCBs into production. But I never tested! Later some improvements where made on the fly which will flow back in a future 0.2 version of the project. 

v0.1 requirements:
==================
* Cheap (I like cheap, I'm Dutch)
* Safe (this is connected to mains, 230V)
* Integration/automation via Node-RED.
* Connected to my home MQTT automation bus.
* Able to individually control each roller shutter or sun screen.
* Drive multiple roller shutters with one PCB.
* Integrated PSU, no external PSU to feed the PCB.

Motorizing the roller shutters:
===============================
A friend gave me a great tip, cheap high quality (10 years guaranty) roller shutter motors from Germany. The tube motors to motorize the roller shutters where relatively easy to fit, that was the easy part of the project. As reference I show you the invoice of the order I placed in case you plan a similar project. The tube motors I used: `JAROLIFT Typ SL 35 / 45`

![jarolift](images/jarolift.png?raw=true)
![invoice](images/invoice.png?raw=true)

Puting the necessary cabling in the wall to drive the roller shutter motors was a whole other story. I was "lucky" that the plastering within the whole house had to be redone. That gave me the opportunity to mill all needed slots to fit the tubing and cabling. In hindsight this was a hell of a job. These photos show some examples of the work in progress:

![wall-cabeling](images/wall-cabeling.png?raw=true)
![kitchen-roller-shutter-cabling](images/kitchen-roller-shutter-cabling.png?raw=true)

Where possible I brought the roller shutter cabling to a central point. Where this was impossible I mounted a box with the controller to the wall which is hidden behind the curtains. The following photos show the before and after situation and also the controller box hidden behind the curtains.

![living-room-before-after](images/living-room-before-after.png?raw=true)
![living-room-roller-shutter-controller](images/living-room-roller-shutter-controller.png?raw=true)
![living-room-roller-shutter-contoller-open-box](images/living-room-roller-shutter-contoller-open-box.png?raw=true)

Most of the roller shutter cabling I could bring into a central location:

![central-location-roller-shutter-controller](images/central-location-roller-shutter-controller.png?raw=true)

The electronics:
================

I will not publish the full design, Gerber files etc. I do not recommend to build the v0.1 version. But still there is a lot to learn. Lets start with ***what I learned***:

* The used ESP32 `DOIT ESP32 DEVKIT V1` drew more current than expected. Or the PCB PSU `HLK-10M12` was just to small (just on top of the specs, sometimes it worked, sometimes it didn't) which resulted in a unstable system (it took me some time to discover what was going on). 
* The used ESP32 became much more hot than expected. 
* Next to the ESP32 itself the power regulator part of the ESP32 board was fed with 12V which made the regulator extremely hot (although within specs, I don't like that hot electronics).
* The integrated PSU also became very hot because of the large power draw of the ESP32.

This made me desolder the ESP32s and replace it with ESP8266s. After this modification the system worked perfectly. I also added a buck step down converter to adapt the 12V to the ESP8266 needs.

* In the relay driver circuit shown below I didn't add LED indicators. Using a LED with every relay will make programming a lot easier.
* I must be able to manually power down each controller PCB. I learned this the hard way: during a freezing cold winter your roller shutters may get completely stuck due to ice formation. I thought I anticipated by leaving my roller shutters open during this period. I did this by modifying the software in NodeRED (I thought). I'm running NodeRED in the cloud and something really odd happened. My NodeRED VM was rebooted (which never happened before). And somehow this triggered all the roller shutters to close (at 2:04 am). One of my roller shutters got completely destroyed. 

The V0.2 versions must include relay indicator LEDs and a "hard" power off button.

* Fuse (F6) is overkill, see below.
* Relay burn-in: the used relays work great but easily burn-in and get stuck. xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

### The power circuit:

To secure the power circuit I followed the recommendations from the manufacturer: fuse 0.5A (F2), thermal fuse which triggers at 73 degrees Celsius (F8) and a 10D561K varistor (R32) to protect the circuit against mains voltage peaks.

![power-psu-scematic](images/power-psu-scematic.png?raw=true)

Fuse (F6) needs some explanation and may even not be necessary: Trace `Ls` feeds the the roller shutter motors, the trace on the PCB is designed to handle a peak current of 10A. The idea was to protect the PCB against over current. But each of the motors are also protected by a fuse of 2.0A (F1 below for example). The total current flowing through this trace can not be more than 3x2.0A = 6.0A. I will leave fuse (F6) out in the v0.2 design.

### The relay driver circuit:

Relay (K1) function is to turn the roller shutter motor on or off. Relay (K2) 

![roller-shutter-relay-scematic](images/roller-shutter-relay-scematic.png?raw=true)


![pcb-v01](images/pcb-v01.png?raw=true)

![esp32-scematic](images/esp32-scematic.png?raw=true)
![PCB-design](images/PCB-design.png?raw=true)











