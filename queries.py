# Run para ejecutar queries paprika en el database
import glob
import logging
import os
import subprocess
import sys


LOG_FILE = "paprika.log"
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,filename=LOG_FILE,format='%(asctime)s - %(message)s')


def logging_call(popenargs, **kwargs):
    process = subprocess.Popen(popenargs, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def check_io():
        while True:
            output = process.stdout.readline().decode()
            if output:
                logger.log(logging.INFO, output)
            else:
                break

    while process.poll() is None:
        check_io()


def main(jar, db):
    logging_call(
        ['java', '-Xmx2G', '-XX:+UseConcMarkSweepGC', '-jar', jar, 
        'query', '-db', db, '-d', '-r', 'ALLAP']
    ) 
        

if __name__ == "__main__":
    try:
        curr_dir = os.getcwd()
        step = os.sep
        jar = f'{curr_dir}{step}paprika{step}build{step}libs{step}Paprika.jar'
        db = f'{curr_dir}{step}{sys.argv[1]}'
        print(db)
        main(jar, db)
    except KeyboardInterrupt:
        logging.warning("Stopping...")