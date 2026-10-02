 PySpark CI/CD & Automated Testing Pipeline



 Project Overview
This project implements a robust PySpark data-processing function (`clean_data`) designed for e-commerce order analytics[cite: 6, 7]. To ensure code quality and production-readiness, a complete **Continuous Integration (CI)** pipeline is established using **GitHub Actions** and **PyTest**[cite: 6, 7].

---
 Project Structure
```text
spark-project/
├── .github/
│   └── workflows/
│       └── pyspark-ci.yaml      # Automated CI pipeline configuration
├── pyspark_job.py               # Core PySpark transformation logic
├── test_orders_pyspark_job.py   # PyTest unit testing suite
└── requirements.txt             # Project dependencies[cite: 6]

Core Data Engineering Logic (pyspark_job.py)
The data cleaning function performs the following transformations:

Filters out records where amount <= 0[cite: 6].

Removes rows with NULL or missing customer name[cite: 6].

Calculates a new metric amount_with_tax by applying a 20% tax rate (amount * 1.20)[cite: 6].


