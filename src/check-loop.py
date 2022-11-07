import time

from COM import COM
from src import get_logger, logger_timing


@logger_timing()
def main():
    """Check by looping the serial cable."""

    logger = get_logger()

    s1 = COM(port="/dev/ttySC0", baudrate=460800)
    s2 = COM(port="/dev/ttySC1", baudrate=460800)

    try:
        logger.info("Start Checking Loop")
        while True:
            s1.sendString("Hello\r\n")
            s2_received = s2.receive()
            s2_check = s2_received == b"Hello\r\n"
            logger.log("COM2", f"{s2_received=}: {'OK' if s2_check else 'NG'}")

            s2.sendString("World\r\n")
            s1_received = s1.receive()
            s1_check = s1_received == b"World\r\n"
            logger.log("COM1", f"{s1_received=}: {'OK' if s1_check else 'NG'}")

            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Exiting...")
        exit()
    finally:
        logger.info("Closing...")
        s1.close()
        s2.close()


if __name__ == "__main__":
    main()
