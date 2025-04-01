# 🚗 Fleetlytics: Scalable Vehicle Fleet Analytics System

Fleetlytics is a mock data engineering project simulating the backend of a shared vehicle platform. It demonstrates how to build real-time, cloud-based pipelines that ingest and process operational data from a fleet of vehicles, enabling business insights through Athena and dashboards.

## 🔧 Tech Stack

- Python
- AWS S3, Glue, Athena
- SQL
- JSON / CSV
- Jupyter Notebook (for visualization)

## 📦 Features

- Ingest vehicle GPS, trip, and maintenance data via simulated API feeds
- ETL pipeline using AWS Glue to process raw data into structured tables
- Query-ready datasets in Athena for operational KPIs
- Dashboard for vehicle utilization, fuel consumption, and maintenance trends

## 📁 Folder Overview

- `data/`: Simulated source files (GPS logs, trip logs, maintenance records)
- `etl/`: Glue ETL script and schema definitions
- `queries/`: Athena SQL queries for fleet metrics
- `dashboard/`: Jupyter notebook with visualizations

## 📊 Example KPIs

- Average trip duration per day
- Vehicle utilization rate
- Maintenance frequency by vehicle
- Idle time and fuel efficiency

## 📌 Note

This is a personal project and does not contain real vehicle data. All datasets are synthetic.
