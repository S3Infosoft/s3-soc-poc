from opencensus.ext.azure.log_exporter import AzureLogHandler
from random import choice
from random import randint
from time import sleep
from sys import argv
from sys import exit
import logging

logger = logging.getLogger(__name__)


def generate_exception():
    exception_list = ['ArithmeticError', 'SecurityError', 'FloatingPointError', 'OverflowError', 'ZeroDivisionError', 'AssertionError', 'AttributeError', 'BufferError','EOFError', 'ImportError', 'ModuleNotFoundError', 'LookupError', 'IndexError', 'KeyError', 'MemoryError', 'NameError', 'UnboundLocalError', 'OSError', 'BlockingIOError', 'ChildProcessError', 'ConnectionError', 'BrokenPipeError', 'ConnectionAbortedError', 'ConnectionRefusedError', 'ConnectionResetError', 'FileExistsError', 'FileNotFoundError', 'InterruptedError', 'IsADirectoryError', 'NotADirectoryError', 'PermissionError', 'ProcessLookupError', 'TimeoutError', 'ReferenceError', 'RuntimeError', 'NotImplementedError', 'RecursionError']
    properties = {'custom_dimensions': {'Message': choice(exception_list)} }
    logger.warning(randint(1, 500), extra=properties)


def main():
    if len(argv) < 2:
        print("Instrumentation key not provided, exiting.")
        exit()
    logger.addHandler(AzureLogHandler(connection_string='InstrumentationKey=' + argv[1]))
    print('Generating telemetry data...')
    while True:
        generate_exception()
        sleep(0.1)


if __name__ == "__main__":
    main()
