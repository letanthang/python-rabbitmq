example with rabbitmq in python

#init venv
python3 -m venv .env
source .env/bin/activate
#install pika
pip install pika --upgrade



#logs : save to file
python receive_log.py > logs_from_emit.log
