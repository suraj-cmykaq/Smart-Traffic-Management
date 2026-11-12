# Smart Traffic Management System 🚦

A Python-based Smart Traffic Management System that simulates traffic flow at intersections using Object-Oriented Programming, intelligent traffic controllers, and emergency vehicle prioritisation.

## 🚀 Features

- Multiple vehicle types: Cars, Bikes, Buses, and Emergency Vehicles.
- Traffic light state management.
- Fixed-time traffic control.
- Density-based traffic control.
- Emergency vehicle prioritisation.
- Real-time traffic simulation.
- Observer pattern for traffic event notifications.
- Factory pattern for vehicle creation.
- JSON data persistence.
- CSV report generation.
- Logging and exception handling.
- Automated unit testing.

## 🏗️ Project Architecture

```text
Smart-Traffic-Management/
│
├── controllers/
├── data/
├── logs/
├── patterns/
├── simulation/
├── storage/
├── tests/
├── traffic/
├── vehicles/
│
├── config.py
├── logger.py
├── main.py
├── traffic_exceptions.py
└── README.md
```

## 🧠 OOP Concepts Implemented

- **Encapsulation:** Protecting and validating vehicle attributes.
- **Inheritance:** Specialised vehicle classes inherit from the base Vehicle class.
- **Polymorphism:** Different vehicle types implement their own behaviour.
- **Abstraction:** Abstract base classes define common interfaces.
- **Factory Pattern:** Centralised vehicle object creation.
- **Observer Pattern:** Event-based traffic notifications.
- **Strategy Pattern:** Interchangeable traffic control strategies.

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming
- JSON
- CSV
- Python Logging
- Unit Testing

## ▶️ How to Run

1. Clone the repository.
2. Open the project folder in VS Code.
3. Run the simulation:

```bash
py main.py
```

4. Run automated tests:

```bash
py -m unittest discover -s tests -v
```

## 📊 Data Storage

The system generates:

- `data/traffic_data.json` – Traffic simulation data.
- `data/road_report.csv` – Road-wise traffic report.
- `logs/traffic_management.log` – Application logs.

## 🧪 Testing

The project includes automated unit tests for vehicles, traffic lights, traffic controllers, and simulation behaviour.

Run the test suite using:

```bash
py -m unittest discover -s tests -v
```

## 🎯 Project Objective

To demonstrate advanced Python OOP concepts through a modular traffic management simulation that handles traffic flow, emergency prioritisation, event notifications, and persistent data storage.

---

**Developed as an independent Python portfolio project.**