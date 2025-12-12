# Opdracht 1: ROS2 Battery Monitor

Dit project demonstreert eenvoudige ROS2-communicatie tussen twee nodes:

- **Battery Publisher** – publiceert een batterijspanning als `Float32`
- **Battery Subscriber** – ontvangt de spanning en geeft een waarschuwing wanneer de batterij laag is

Dit Opdracht heb ik gemaakt **zonder een fysieke robot**. De reden is dat de Raspberry Pi van de robot Jessie gebruikt, terwijl mijn systeem ROS2 Humble draait, en deze twee niet compatibel zijn.
Daarom gebeurt de volledige demonstratie van deze opdracht via de terminal op mijn eigen ROS2-omgeving.

**Ook heb ik de opdracht licht aangepast:**

De echte robotbatterij werd niet gebruikt, dus de batterijwaardes worden gesimuleerd door mijn publisher node.

In plaats van elke minuut te publishen, heb ik de interval verkort naar elke 2 seconden, zodat de werking tijdens testen en demonstreren sneller zichtbaar is.

De subscriber reageert wel correct volgens de opdracht (waarschuwing), maar dan op de gesimuleerde data.

## Installatie & Build

Ga naar je workspace:

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```
## Nodes handmatig uitvoeren

1. Start de publisher
```bash
ros2 run my_robot_pkg battery_publisher
```
2. Start de subscriber (in een tweede terminal)
```bash
ros2 run my_robot_pkg battery_subscriber
```
## Topics bekijken

Lijst van actieve topics:
```bash
ros2 topic list
```
Topicinhoud live bekijken:
```bash
ros2 topic echo /battery_voltage
```
## Launch file gebruiken (publisher + subscriber samen)
```bash
ros2 launch my_robot_pkg my_robot_pkg_launch_file.launch.py
```
