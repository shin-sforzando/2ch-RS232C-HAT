import serial


class COM:
    def __init__(
        self,
        port="/dev/ttySC0",
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
    ):
        self.ser = serial.Serial(
            port=port, baudrate=baudrate, parity=parity, stopbits=stopbits, timeout=0.1
        )
        self.ser.flushInput()

    def sendByte(self, data):
        self.ser.write(data.encode("ascii"))

    def sendString(self, data):
        self.ser.write(data.encode("ascii"))

    def receive(self):
        if 0 < self.ser.inWaiting():
            data = self.ser.readline()
            return data

    def receiveByte(self):
        return self.ser.serial.read(size=1).decode("utf-8")

    def close(self):
        self.ser.close()
