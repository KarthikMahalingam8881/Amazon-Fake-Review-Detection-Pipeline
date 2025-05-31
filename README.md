# Amazon-Fake-Review-Detection-Pipeline
This project builds a scalable and modular data pipeline to detect fake or suspicious Amazon product reviews using NLP techniques. The pipeline uses AWS Glue for data cleaning and Apache Airflow for orchestration. It processes data stored in Amazon S3 and outputs enriched sentiment insights back into S3.

---

## 🚀 Pipeline Overview
[Raw JSON Reviews in S3]

⬇️
[Glue Crawler] — infers schema
⬇️
[Glue Spark ETL Job] — cleans and transforms raw data
⬇️
[Cleaned Parquet in S3 (/processed/year=2023)]
⬇️
[Dockerized NLP Script] — sentiment analysis
⬇️
[NLP Output to S3 (/processed/nlp/year=2023/)]

---

## ⚙️ Tools & Technologies

- **Amazon S3** – Raw + processed data storage
- **AWS Glue** – Schema inference + PySpark ETL
- **Apache Airflow** – Workflow orchestration
- **Docker** – NLP step containerization
- **Boto3** – Access S3 via Python
- **spaCy / TextBlob** – Sentiment analysis

---

## 🗂️ Folder Structure
📁 dags/
└── s3_glue_nlp_pipeline.py # Airflow DAG to orchestrate NLP job

📁 nlp_pipeline/
├── nlp_processing.py # Python script for sentiment analysis
├── Dockerfile # Container for running NLP logic
└── requirements.txt # Python dependencies

📁 airflow-docker/ (optional)
└── docker-compose.yaml # Local Airflow setup

---

## 🧪 How to Run (Simplified)

### 1. 📦 NLP Step Locally (Test It)
# Build the container
docker build -t nlp-review .

# Run it
docker run --rm --env-file ../aws.env nlp-review

## 🛰 Orchestrate via Airflow
Add s3_glue_nlp_pipeline.py to your dags/ folder

Use DockerOperator or PythonOperator to run the NLP container

Start your Airflow UI and trigger the DAG

## 📌 Notes
Glue Job must be created on AWS Console manually, with the PySpark script pointing to the raw data

AWS credentials should be shared via environment variables or .env (DO NOT commit to GitHub)

Sample .env.example can be added for format reference



