import logging, sys


def setup_logger():
  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)

  sh = logging.StreamHandler(sys.stdout)
  formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S'
  )
  sh.setFormatter(formatter)
  logger.addHandler(sh)
  return logger

if __name__ == '__main__':
  logger = setup_logger()
  logger.info('test log')
