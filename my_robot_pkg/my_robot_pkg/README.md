# ROS2 Opdrachten

##  Opdracht 1:
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

--------------------------------------------------

# Opdracht 2 & 3 – ROS2 Keyboard Control

In deze opdrachten wordt de robot bestuurd via toetsenbordcommando’s met **ROS2-nodes**.

## Overzicht

- **Keyboard Publisher** – leest toetsenbordinput en verstuurt commando’s.  
- **CmdVel Subscriber** – ontvangt deze commando’s en zet ze om naar beweging (`/cmd_vel`).  
 
De demonstratie gebeurt volledig via **terminal** en **Gazebo** binnen de **ROS2 Humble**-omgeving.

---

## Opdracht 2

De robot kan bewegen met volgende toetsen:

| Toets | Actie     |
|:------|:-----------|
| `z` | Vooruit |
| `s` | Achteruit |
| `a` | Links |
| `e` | Rechts |

De **publisher** draait op de host-pc, en de **subscriber** stuurt de bewegingscommando’s door naar de robot in **Gazebo**.

---

## Opdracht 3 – Uitbreiding

In deze uitbreiding worden de commando’s omgezet naar **velocity-commando’s** in plaats van **distance-commando’s**.

De robot blijft rijden zolang er een snelheid actief is.

| Toets | Actie |
|:------|:------|
| `z` | Snelheid +5 |
| `s` | Snelheid −5 |
| `a` | Linker wiel sneller, rechter wiel trager |
| `x` | Direct stoppen (`V 0 0`) |

De snelheid wordt intern bijgehouden en omgezet naar het berichttype **`geometry_msgs/Twist`**.

---

## Installatie & Build

Ga naar je workspace:

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

## Nodes handmatig uitvoeren

1. Start Gazebo
```bash
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

2. Start de keyboard publisher
```bash
ros2 run my_robot_pkg keyboard_publisher
```
3. Start de cmd_vel subscriber (in een tweede terminal)
```bash
ros2 run my_robot_pkg cmdvel_subscriber
```
