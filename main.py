import sys
from shaen_logger import slog
import logging


def main():
    slog.info("Yo")


if __name__ == '__main__':
    try:
        if isinstance(slog, logging.Logger):
            main()
    except ValueError as e:
        print(f"There is a failure referencing slog from shaen_logger: {e}")
        sys.exit(1)

