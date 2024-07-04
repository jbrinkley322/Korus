from airflow import DAG
import datetime
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


def test():
    print('###' * 10)
    print()
    print(f'test {datetime.datetime.now()}')
    print()
    print('###' * 10)
    return 1


dag = DAG('test', description='test',
          schedule_interval='*/1 * * * *',
          start_date=datetime.datetime(2020, 1, 1), catchup=False)

start_step = DummyOperator(task_id="start_step", dag=dag)

test_step = PythonOperator(task_id="test_step",
                            python_callable=test,
                            dag=dag)

end_step = DummyOperator(task_id="end_step", dag=dag)

start_step >> test_step >> end_step
