FROM apache/airflow:2.7.2-python3.10

# Switch to airflow user early
USER airflow

# Install Python packages as airflow user
RUN pip install --no-cache-dir boto3 textblob nltk pandas pyarrow

# Download NLTK data
RUN python -m nltk.downloader stopwords punkt wordnet