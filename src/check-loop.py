import time

from loguru import logger

from COM import COM


def main():
    logger.add("logs/check-loop_{time}.log")

    s1 = COM(port="/dev/ttySC0", baudrate=460800)
    s2 = COM(port="/dev/ttySC1", baudrate=460800)

    try:
        logger.info("Start Checking Loop")
        while True:
            s1.sendString("Hello")
            s2_received = s2.receive()
            print(f"{s2_received}: {'OK' if s2_received == b'Hello' else 'NG'}")
            s2.sendString("World")
            s1_received = s1.receive()
            print(f"{s1_received}: {'OK' if s1_received == b'Hello' else 'NG'}")
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
