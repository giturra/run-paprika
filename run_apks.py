# Run para ejecutar paprika apk by apk
import glob
import logging
import os
import subprocess
import sys


def get_all_apks(folder):
    print(f'{folder}{os.sep}*.apk')
    return glob.glob(f'{folder}{os.sep}*.apk')

# print(get_all_apks(f'{os.getcwd()}{os.sep}{sys.argv[1]}'))
LOG_FILE = "paprika.log"
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,filename=LOG_FILE,format='%(asctime)s - %(message)s')


def logging_call(popenargs, num, apkname, **kwargs):
    logging.log(logging.INFO, f'Se esta analizando el apk {apkname} número {num}')
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
    logging.log(logging.INFO, f'Se términa el análisis el apk {apkname} número {num}')


def main(jar, plaforms, db, apks):
    for i in range(len(apks)):
        logging_call(
            ['java', '-Xmx2G', '-XX:+UseConcMarkSweepGC', '-jar', jar, 'analyse', '-a', platforms, '-db', db, apks[i]],
            i+1,
            apks[i] 
        )


if __name__ == "__main__":
    try:
        curr_dir = os.getcwd()
        step = os.sep
        jar = f'{curr_dir}{step}paprika{step}build{step}libs{step}Paprika.jar'
        platforms = sys.argv[3]
        apks = f'{curr_dir}{step}{sys.argv[1]}'
        apks = get_all_apks(apks)
        db = f'{curr_dir}{step}{sys.argv[2]}'
        main(jar, platforms, db, apks)
    except KeyboardInterrupt:
        logging.warning("Stopping...")