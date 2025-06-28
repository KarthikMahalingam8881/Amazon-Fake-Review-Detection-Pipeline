# Amazon-Fake-Review-Detection-Pipeline
This project implements a scalable, modular data pipeline to detect fake or suspicious Amazon product reviews using NLP techniques. It leverages AWS Glue for ETL, Amazon S3 for storage, Docker for containerized sentiment analysis, and Apache Airflow for orchestration.

----
 [Read the full project breakdown on Medium](https://medium.com/@kmahali2/detecting-fake-amazon-reviews-using-a-scalable-aws-data-pipeline-s3-glue-airflow-nlp-0157143206e1)
----
## 🚀 Pipeline Overview
![image](https://github.com/user-attachments/assets/3df50fe3-b444-4538-8874-4be06aac358f)


---

## ⚙️ Tools & Technologies

- **Amazon S3** – Raw + processed data storage
- **AWS Glue** – Schema inference & PySpark-based ETL
- **Apache Airflow** – Workflow orchestration
- **Docker** – Containerized NLP step
- **spaCy** / **TextBlob** – Sentiment analysis
- **Boto3** – Python SDK for AWS

---

## 🗂️ Folder Structure

airflow-docker/

├── dags/

│ └── s3_glue_nlp_pipeline.py # Airflow DAG for orchestrating NLP task

├── nlp_job/

│ ├── nlp_processing.py # Python script for sentiment tagging

│ ├── Dockerfile # NLP Docker image

│ └── requirements.txt # Python dependencies

├── docker-compose.yaml # Local Airflow setup

└── config/, plugins/, logs/ # Support files and outputs

---

## 🧪 How to Run (Simplified)

### 1. 📦 NLP Step Locally (Test It)
# Build the container
docker build -t nlp-review ./nlp_job

# Run it (pass AWS credentials via env file)
docker run --rm --env-file ../aws.env nlp-review

## Run Full Pipeline via Airflow
* Add s3_glue_nlp_pipeline.py to your Airflow dags/ folder

* Use DockerOperator or PythonOperator to run the NLP container

* Start the Airflow UI and trigger the DAG

## 📌 Notes
Glue Job must be created on AWS Console manually, with the PySpark script pointing to the raw data

AWS credentials should be shared via environment variables or .env (DO NOT commit to GitHub)




