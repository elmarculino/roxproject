import datetime

from airflow import DAG
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator

import sql_statements


dag = DAG(
    'create_rox_tables',
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

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

start_operator >> drop_tables
drop_tables >> create_person_table
create_person_table >> create_product_table
create_product_table >> create_customer_table
create_customer_table >> create_salesorderheader_table
create_salesorderheader_table >> create_specialofferproduct_table
create_specialofferproduct_table >> create_salesorderdetail_table
create_salesorderdetail_table >> end_operator
