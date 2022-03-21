import sys
from shaen_logger.log import print_output
from shaen_logger import slog
import logging


def main():
    # # slog.info("Yo")
    # print_output()
    slog.info("=" * 20)
    slog.info("STARTING NEW EXECUTION...")
    slog.info("Running main.py")
    slog.info("=" * 20)


if __name__ == '__main__':
    try:
        if isinstance(slog, logging.Logger):
            main()
    except ValueError as e:
        print(f"There is a failure referencing slog from shaen_logger: {e}")
        sys.exit(1)

