import datetime

from airflow import DAG
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator

import sql_statements

def load_data_to_redshift(sql_stmt, *args, **kwargs):
    redshift_hook = PostgresHook("redshift")
    redshift_hook.run(sql_stmt)

dag = DAG(
    'stage_rox_bike_tables',
    start_date=datetime.datetime.now()
)

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

drop_tables = PostgresOperator(
    task_id="drop_tables",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.DROP_TABLES_SQL
)

create_person_table = PostgresOperator(
    task_id="create_person_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.CREATE_PERSON_TABLE_SQL
)

create_product_table = PostgresOperator(
    task_id="create_product_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.CREATE_PRODUCT_TABLE_SQL
)

create_customer_table = PostgresOperator(
    task_id="create_customer_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.CREATE_CUSTOMER_TABLE_SQL
)

create_salesorderheader_table = PostgresOperator(
    task_id="create_salesorderheader_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.CREATE_SALESORDERHEADER_TABLE_SQL
)

create_specialofferproduct_table = PostgresOperator(
    task_id="create_specialofferproduct_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.CREATE_SPECIALOFFERPRODUCT_TABLE_SQL
)

create_salesorderdetail_table = PostgresOperator(
    task_id="create_salesorderdetail_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.CREATE_SALESORDERDETAIL_TABLE_SQL
)

copy_person_task = PythonOperator(
    task_id='load_person_from_s3_to_redshift',
    dag=dag,
    python_callable=load_data_to_redshift,
    op_kwargs={'sql_stmt': sql_statements.COPY_PERSON_SQL }
)

copy_product_task = PythonOperator(
    task_id='load_product_from_s3_to_redshift',
    dag=dag,
    python_callable=load_data_to_redshift,
    op_kwargs={'sql_stmt': sql_statements.COPY_PRODUCT_SQL }
)

copy_customer_task = PythonOperator(
    task_id='load_customer_from_s3_to_redshift',
    dag=dag,
    python_callable=load_data_to_redshift,
    op_kwargs={'sql_stmt': sql_statements.COPY_CUSTOMER_SQL }
)

copy_salesorderheader_task = PythonOperator(
    task_id='load_salesorderheader_from_s3_to_redshift',
    dag=dag,
    python_callable=load_data_to_redshift,
    op_kwargs={'sql_stmt': sql_statements.COPY_SALESORDERHEADER_SQL }
)

copy_specialofferproduct_task = PythonOperator(
    task_id='load_specialofferproduct_from_s3_to_redshift',
    dag=dag,
    python_callable=load_data_to_redshift,
    op_kwargs={'sql_stmt': sql_statements.COPY_SPECIALOFFERPRODUCT_SQL }
)

copy_salesorderdetail_task = PythonOperator(
    task_id='load_salesorderdetail_from_s3_to_redshift',
    dag=dag,
    python_callable=load_data_to_redshift,
    op_kwargs={'sql_stmt': sql_statements.COPY_SALESORDERDETAIL_SQL }
)
end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

start_operator >> drop_tables
drop_tables >> create_person_table
create_person_table >> create_product_table
create_product_table >> create_customer_table
create_customer_table >> create_salesorderheader_table
create_salesorderheader_table >> create_specialofferproduct_table
create_specialofferproduct_table >> create_salesorderdetail_table
create_salesorderdetail_table >> copy_person_task
copy_person_task >> copy_product_task
copy_product_task >> copy_customer_task
copy_customer_task >> copy_salesorderheader_task
copy_salesorderheader_task >> copy_specialofferproduct_task
copy_specialofferproduct_task >> copy_salesorderdetail_task
copy_salesorderdetail_task >> end_operator
