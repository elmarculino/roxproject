from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.rox_plugin import StageToRedshiftOperator, DataQualityperator


default_args = {
    'owner': 'roxproject',
    'start_date': datetime(2019, 1, 12),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes = 5),
    'catchup' : False,
    'email_on_retry': False
}

dag = DAG('rox_bike_etl_dag',
          default_args=default_args,
          description='Load data to Redshift with Airflow',
          schedule_interval='0 * * * *'
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

stage_events_to_redshift = StageToRedshiftOperator(
    task_id='stage_person',
    dag=dag,
    redshift_conn_id="redshift",
    iam_role="iam_role",
    table="Person",
    s3_bucket="roxproject",
    s3_key="data/Person.Person.csv",
    provide_context=True
)

stage_songs_to_redshift = StageToRedshiftOperator(
    task_id='stage_product',
    dag=dag,
    redshift_conn_id="redshift",
    iam_role="iam_role",
    table="Product",
    s3_bucket="roxproject",
    s3_key="data/Production.Product.csv",
    provide_context=True
)

run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    redshift_conn_id="redshift",
    tables=['Person']
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

start_operator >> [stage_person_to_redshift, stage_product_to_redshift]

[stage_person_to_redshift, stage_product_to_redshift] >> run_quality_checks

run_quality_checks >> end_operator
