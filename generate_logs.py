import logging
import time
from   random import randint
import os


def main():
    
    # Variables For simulate logs

    time_to_wait_s       = 2
    logs_file_name       = 'example.log'
    limit_size_file_beat = 150
    

    # Log configurations

    logging.basicConfig(
         filename= logs_file_name,
         level=logging.INFO, 
         format= '%(asctime)s | %(pathname)s:%(lineno)d | %(levelname)s | %(message)s',
         datefmt='%m/%d/%Y %I:%M:%S %p'
     )
    
    # Time of sleep
    time.sleep(time_to_wait_s)
    
    LOGING_TYPE = [
                "logging.debug('debug message')",
                "logging.info('OK Access to database')",
                "logging.info('OK Access to Good Connections')",    
                "logging.info('OK Backup of DB')",
                "logging.info('OK Loggin Access')",    
                "logging.warning('Fail Request')",
                "logging.error('error Request')",
                "logging.critical('Dont access to DB')",
                "logging.critical('Dont work of sistems')"
                   ]    
                   
    log = randint(0,len(LOGING_TYPE)-1)

    eval(LOGING_TYPE[log])

    size = os.path.getsize(logs_file_name)

    print("SIMULATE LOG: ", log, " ", LOGING_TYPE[log], "SIZE: ",size)

while True == True:
    main()