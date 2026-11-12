# 🚦 NEXUS — Smart Traffic Management System

<p align="center">
  <strong>AI-Powered Traffic Simulation & Intelligent Traffic Control</strong>
</p>

<p align="center">
  A Python-based Smart Traffic Management System combining Object-Oriented Programming, Machine Learning, adaptive traffic control, and an interactive Cyberpunk-style dashboard.
</p>

---

## 🌐 Project Overview

**NEXUS** is an intelligent traffic intersection simulation designed to demonstrate how software engineering and machine learning can work together to analyze and manage traffic conditions.

The system simulates a four-road intersection, monitors vehicle density, prioritizes emergency vehicles, and uses a Random Forest classification model to identify traffic congestion levels.

It also includes an interactive Streamlit dashboard for monitoring the simulation, exploring AI predictions, and analyzing historical traffic data.

> **Project type:** Python | OOP | Machine Learning | Streamlit | Data Analytics

---

## ✨ Key Features

### 🚦 Intelligent Traffic Simulation
- Four-road traffic intersection simulation.
- Vehicle movement and traffic signal state management.
- Fixed-time and density-based traffic control strategies.
- Emergency vehicle prioritization.
- Modular and extensible simulation architecture.

### 🧠 Machine Learning Intelligence
- Random Forest congestion classification.
- Four congestion categories: LOW, MEDIUM, HIGH, and CRITICAL.
- Traffic density and vehicle composition analysis.
- Model training, evaluation, and prediction using Scikit-learn.
- Model persistence using Joblib.

### 💻 NEXUS Cyberpunk Dashboard
- Dark futuristic interface with neon-inspired styling.
- Interactive traffic monitoring.
- System overview and KPI cards.
- AI congestion prediction display.
- Individual road monitoring.
- Vehicle composition analytics.
- Historical traffic data visualization.
- Simulation controls directly from the dashboard.

### 🛡️ Software Engineering Features
- Object-Oriented Programming.
- Exception and error handling.
- File handling and data persistence.
- Structured application logging.
- JSON and CSV reporting.
- Automated unit testing.

---

## 🖥️ Dashboard

The NEXUS dashboard is built using Streamlit and provides an interactive interface for exploring the traffic simulation.

### Dashboard Modules

| Module | Description |
|---|---|
| Overview | Traffic statistics, road status, and simulation cycles |
| AI Intelligence | Random Forest congestion predictions |
| Road Monitoring | Individual road and vehicle composition analysis |
| Analytics | Historical traffic observations and visualizations |

**Dashboard preview:** Add your actual dashboard screenshots here as the project develops.

---

## 🧠 Machine Learning Workflow

NEXUS uses a **Random Forest Classifier** from Scikit-learn to classify traffic congestion.

### Workflow

1. Generate synthetic traffic training data.
2. Prepare traffic-related features.
3. Generate congestion labels using density-based thresholds.
4. Train and evaluate the Random Forest model.
5. Save the trained model using Joblib.
6. Load the model into the traffic AI service.
7. Analyze intersection data and display predictions.

### Congestion Categories

| Category | Description |
|---|---|
| LOW | Low traffic density |
| MEDIUM | Moderate traffic density |
| HIGH | High traffic density |
| CRITICAL | Very high traffic density |

**Important ML limitation:** The current training dataset is synthetic, and its congestion labels are generated using density-based rules. The model demonstrates an end-to-end machine learning workflow, but its evaluation results do not establish real-world traffic prediction accuracy. The displayed maximum class probability is not calibrated confidence.

---

## 🏗️ Project Architecture

```text
Smart-Traffic-Management/
│
├── ai/
│   ├── dataset_generator.py
│   ├── train_model.py
│   ├── predictor.py
│   ├── traffic_ai_service.py
│   ├── traffic_data_collector.py
│   └── traffic_history.py
│
├── controllers/
│   ├── fixed_time.py
│   ├── density_based.py
│   └── emergency_priority.py
│
├── data/
│   └── traffic datasets and reports
│
├── patterns/
│   └── traffic_observer.py
│
├── simulation/
│   └── simulator.py
│
├── storage/
│   └── data_manager.py
│
├── tests/
│   ├── test_controllers.py
│   ├── test_traffic_light.py
│   └── test_vehicles.py
│
├── traffic/
│   ├── road.py
│   ├── intersection.py
│   ├── traffic_light.py
│   └── traffic_network.py
│
├── vehicles/
│   ├── vehicle.py
│   ├── car.py
│   ├── bike.py
│   ├── bus.py
│   └── emergency_vehicle.py
│
├── dashboard.py
├── dashboard_engine.py
├── main.py
├── config.py
├── logger.py
├── traffic_exceptions.py
├── requirements.txt
└── README.md
```

---

## 🧩 OOP Concepts & Design Patterns

This project demonstrates practical implementation of:

- **Encapsulation:** Managing internal object state.
- **Inheritance:** Specialized vehicle classes derived from a common vehicle abstraction.
- **Polymorphism:** Different vehicle and controller behaviors through shared interfaces.
- **Abstraction:** Abstract base classes for common contracts.
- **Strategy Pattern:** Interchangeable traffic control strategies.
- **Factory Pattern:** Centralized vehicle object creation.
- **Observer Pattern:** Event-based communication between traffic components.
- **Modular Architecture:** Separating simulation, AI, storage, and dashboard responsibilities.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Streamlit | Interactive dashboard |
| Scikit-learn | Machine Learning |
| Random Forest | Congestion classification |
| Pandas | Data processing and analytics |
| NumPy | Numerical operations |
| Joblib | Model persistence |
| Matplotlib / Streamlit charts | Data visualization |
| JSON | Structured data persistence |
| CSV | Historical traffic records |
| Logging | Application monitoring |
| Unittest | Automated testing |
| Git & GitHub | Version control |

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/suraj-cmykaq/Smart-Traffic-Management.git
```

### 2. Navigate into the project

```bash
cd Smart-Traffic-Management
```

### 3. Install dependencies

```bash
py -m pip install -r requirements.txt
```

Install Streamlit for the dashboard:

```bash
py -m pip install streamlit
```

### 4. Generate the training dataset

```bash
py -m ai.dataset_generator
```

### 5. Train the ML model

```bash
py -m ai.train_model
```

### 6. Run the traffic simulation

```bash
py main.py
```

### 7. Launch the NEXUS dashboard

```bash
py -m streamlit run dashboard.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

---

## 🧪 Automated Testing

The project includes unit tests for core traffic components and control logic.

Run the complete test suite:

```bash
py -m unittest discover -s tests -v
```

**Current project test status: 38 tests passing.**

---

## ⚠️ Current Scope & Limitations

- The traffic network is a software simulation, not a connection to real-world road infrastructure.
- Traffic observations are generated by the simulation.
- The ML model currently uses synthetic training data.
- The dashboard displays simulation state and updates when simulation cycles are executed.
- The system does not currently consume live traffic sensors, GPS feeds, or external traffic APIs.
- The current ML model classifies congestion; it does not independently control traffic signals.

---

## 🚀 Future Improvements

- Integration with real-world traffic datasets.
- Time-series-based traffic congestion forecasting.
- Live traffic sensor and IoT integration.
- Reinforcement Learning-based traffic signal optimization.
- Multi-intersection traffic coordination.
- Advanced emergency vehicle routing.
- More detailed animated traffic intersection visualization.

---

## 👨‍💻 Developer

**Suraj Chandhariyavi**

B.Tech — Computer Science Engineering  
Generative AI

GitHub: [suraj-cmykaq](https://github.com/suraj-cmykaq)

Project Repository: [Smart Traffic Management System](https://github.com/suraj-cmykaq/Smart-Traffic-Management)

---

<p align="center">
  <strong>Built with Python, Object-Oriented Programming, and Machine Learning.</strong>
</p>

<p align="center">
  🚦 NEXUS — Making Traffic Intelligence Smarter.
</p>