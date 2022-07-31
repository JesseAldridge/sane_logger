import logging, sys


def sane_logger(log_level=logging.INFO):
  logger = logging.getLogger()

  if hasattr(logger, 'sane_logger_called'):
    return logger
  logger.sane_logger_called = True

  logger.setLevel(log_level)

  sh = logging.StreamHandler(sys.stdout)
  formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S %Z'
  )
  sh.setFormatter(formatter)
  logger.addHandler(sh)
  return logger

if __name__ == '__main__':
  logger = sane_logger(logging.DEBUG)
  logger.info('test log')
