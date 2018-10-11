import sys
import argparse
from crontab import CronTab
from logging import getLogger
from logging.config import fileConfig
from datetime import datetime
from os import path
import json
from .alert import Alert


def get_modified_time(*args, **kwargs):
    logger = kwargs.get('logger')
    filepath = kwargs.get('filepath')
    try:
        if path.exists(filepath):
            return path.getmtime(filepath)
        else:
            raise Exception('log file not found error')
    except Exception as e:
        logger.exception(f"issue find with file {filepath} | {e}")
        return False

def main(*args, **kwargs):
    args = kwargs.get('args')
    logger.debug('in main function')
    crons = CronTab(tabfile=args.crontab_path)
    alerts = []
    for job in crons:
        if job.command.strip()[0] == '#':
            continue
        try:
            prev_runtime = job.schedule(date_from=datetime.now()).get_prev().timestamp()
            logger.info(f"{job} must be run at {prev_runtime}")
            log_filepath = job.command.split('>>')[1].split('#')[0].strip()
            logger.debug(f"log filepath is | {log_filepath}")
            mtime = get_modified_time(filepath= log_filepath, logger= logger)
            if mtime:
                logger.info(f"log_filepath last updated at {mtime}")
            else:
                raise Exception(job.command)
            
            if mtime < prev_runtime:
                raise Exception(f"{job.command} | is not working")
        except Exception as e:
            logger.error(e, exc_info=True)
            alerts.append(str(e))
    return alerts


def run():
    global logger
    fileConfig(path.dirname(path.realpath(__file__)) + path.sep + 'logging.conf')
    logger = getLogger()

    logger.debug('script started')

    parser = argparse.ArgumentParser(description='system crontab file path')
    parser.add_argument('-f', type=str, dest='crontab_path', required='True',
                        help='the file path of the crontab file')
    parser.add_argument('-u', '--user', dest='user', type=str, default='root',
                        help='linux username if the crontab is for specific user')

    args = parser.parse_args()
    logger.debug(args.crontab_path)

    alert_msg = json.dumps(main(args = args))
    alert = Alert(logger=logger)
    alert.raiseAlert(alert_msg)