# 🚦 Smart Traffic Management System

An object-oriented Python simulation of an intelligent traffic intersection, combining adaptive traffic control, emergency vehicle prioritization, historical data collection, and Machine Learning-based congestion classification.

## 📌 Project Overview

The Smart Traffic Management System simulates a four-road intersection and analyzes traffic conditions using a Random Forest classification model.

It collects traffic information, identifies congestion levels, prioritizes emergency vehicles, and maintains historical traffic records.

## ✨ Key Features

- **Adaptive Traffic Control:** Multiple traffic control strategies.
- **Emergency Vehicle Priority:** Gives priority to roads containing emergency vehicles.
- **AI Congestion Classification:** Classifies traffic into LOW, MEDIUM, HIGH, and CRITICAL.
- **Traffic Data Collection:** Captures vehicle counts, road density, and vehicle categories.
- **Historical Data Storage:** Stores traffic observations in CSV format.
- **JSON and CSV Reports:** Exports simulation results.
- **Logging System:** Maintains application logs.
- **Exception Handling:** Handles invalid operations and unexpected errors.
- **Automated Testing:** Unit tests for core modules and AI components.

## 🧠 Machine Learning

The project uses a **Random Forest Classifier** from Scikit-learn.

The ML workflow:

1. Generate synthetic traffic training data.
2. Classify congestion levels using density-based labels.
3. Train and evaluate the classification model.
4. Save the trained model using Joblib.
5. Load the model to analyze traffic conditions.
6. Display congestion predictions and model probabilities.

**Note:** The current training dataset is synthetic. The model demonstrates an end-to-end ML workflow, but its evaluation results do not establish real-world traffic prediction accuracy.

## 🏗️ Architecture

```text
Smart Traffic Management
│
├── ai/             Machine Learning and data collection
├── controllers/    Traffic control strategies
├── data/           Traffic datasets and reports
├── logs/           Application logs
├── patterns/       Design patterns
├── simulation/     Traffic simulation engine
├── storage/        JSON and CSV persistence
├── tests/          Automated unit tests
├── traffic/        Roads, signals and intersections
├── vehicles/       Vehicle classes
│
├── config.py
├── logger.py
├── main.py
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming
- Scikit-learn
- Pandas
- NumPy
- Random Forest Classification
- JSON and CSV
- Python Logging
- Unittest

## 🧩 OOP and Design Concepts

- Encapsulation
- Inheritance
- Abstraction
- Polymorphism
- Abstract Base Classes
- Strategy Pattern
- Factory Pattern
- Observer Pattern
- Modular Architecture

## ⚙️ Installation and Setup

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

### 4. Generate the training dataset

```bash
py -m ai.dataset_generator
```

### 5. Train the Machine Learning model

```bash
py -m ai.train_model
```

### 6. Run the simulation

```bash
py main.py
```

## 🧪 Run Tests

Execute the complete automated test suite:

```bash
py -m unittest discover -s tests -v
```

**Current test status:** 38 tests passing.

## 🚀 Future Improvements

- Real-world traffic dataset integration.
- Traffic congestion forecasting using time-series models.
- Interactive traffic monitoring dashboard.
- Real-time sensor data integration.
- Reinforcement Learning-based traffic signal optimization.
- Multi-intersection traffic coordination.

## 👨‍💻 Developer

**Suraj Chandhariyavi**

B.Tech Computer Science Engineering | Generative AI

GitHub: https://github.com/suraj-cmykaq

---

*Developed as an independent Python, OOP, and Machine Learning portfolio project.*