from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from cwl_airflow.utilities.cwl import clean_up_dag_run
from cwl_airflow.utilities.report import dag_on_success, dag_on_failure


# This python file will load automatically when first running "docker-compose up" command.
# Here, I have modified the DAG to simple output DAG context (hopefully to comunicate necessary DAG_run variables)

def clean_dag_run(**context):
    print(context)
    )


dag = DAG(dag_id="clean_dag_run",
          start_date=days_ago(1),
          on_failure_callback=dag_on_failure,
          on_success_callback=dag_on_success,
          schedule_interval=None)


run_this = PythonOperator(task_id="clean_dag_run",
                          python_callable=clean_dag_run,
                          provide_context=True,
                          dag=dag)
