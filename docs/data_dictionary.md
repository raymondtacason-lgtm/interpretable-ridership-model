# Step 2 — Data Understanding

## 2.1 Dataset Overview
The dataset used in this project is composed of two main components: internal workforce scheduling records and external operational context data. The internal dataset contains raw scheduling information such as employee names, assigned stations, and shift start and end times. These records represent the actual staffing assignments across different stations within the transportation network.

To enrich the internal data and provide additional context for forecasting staffing requirements, several external data sources were incorporated. These include the Philippine holiday calendar, historical weather information, and publicly available ridership or demand indicators. These external sources help capture factors that influence staffing needs but are not directly recorded in the internal scheduling system.

## 2.2 Data Dictionary
This data dictionary lists only the raw fields collected from internal systems and external sources.

| Variable Name   | Type     | Description                                      | Source                              |
|-----------------|----------|--------------------------------------------------|-------------------------------------|
| date            | Date     | Schedule date                                   | Internal                            |
| employee_name   | Text     | Employee full name                              | Internal                            |
| station         | Text     | Assigned station or location                    | Internal                            |
| shift_start     | Time     | Start time of scheduled shift                   | Internal                            |
| shift_end       | Time     | End time of scheduled shift                     | Internal                            |
| holiday_date    | Date     | Official PH holiday dates                       | External (PH Gov)                   |
| weather_raw     | Text     | Raw weather description (e.g., Clear, Rain, Cloudy) | External (Weather API / historical data) |
| ridership_raw   | Numeric  | Public demand indicator (e.g., ridership, traffic volume) | External (Transport datasets) |
