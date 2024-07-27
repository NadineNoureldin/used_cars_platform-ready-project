from airflow.operators.empty import EmptyOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.contrib.operators.gcs_list_operator import GoogleCloudStorageListOperator
from airflow import DAG
from datetime import datetime

dag = DAG(
    dag_id="final_project_gcs_to_bigquery_Nadine",
    description="Transfer data from GCS to bigquery",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
)

start_task = EmptyOperator(task_id="start_task", dag=dag)

load_csv = GCSToBigQueryOperator(
    task_id="final_project_gcs_to_bigquery",
    bucket="ready-project-dataset",
    field_delimiter = ';',
    source_objects=["cars-com_dataset/*csv"],
    skip_leading_rows = 1,
    source_format = 'CSV',
    max_bad_records = 100000000,
    ignore_unknown_values = True,
    destination_project_dataset_table="ready-data-de24.landing_Nadine.used_cars_platform",
    autodetect=True,
    write_disposition="WRITE_TRUNCATE",
    dag=dag
)

end_task = EmptyOperator(task_id="end_task", dag=dag)


start_task >> load_csv >> end_task