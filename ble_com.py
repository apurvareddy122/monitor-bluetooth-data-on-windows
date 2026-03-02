import asyncio
from bleak import BleakScanner, BleakClient

# Nordic UART Service UUIDs
NUS_TX_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
NUS_RX_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"

DEVICE_NAME = "Nordic_UART" 

# File Logging Enable
LOG_TO_FILE = False


def notification_handler(sender, data):
    message = data.decode("utf-8", errors="ignore")
    print(message, end="")  
    print("\n")

    if LOG_TO_FILE:
        with open("ble_raw_data.txt", "a") as f:
            f.write(message)


async def main():
    print("Scanning for BLE devices...")
    devices = await BleakScanner.discover()

    target = None
    for d in devices:
        if d.name and DEVICE_NAME in d.name:
            target = d
            break

    if not target:
        print("Device not found!")
        return

    print(f"Connecting to {target.name}...")

    async with BleakClient(target.address) as client:
        print("Connected!")

        await client.write_gatt_char(NUS_RX_UUID, b"START\n", response=False)

        await client.start_notify(NUS_TX_UUID, notification_handler)

        print("Receiving raw BLE data... Press Ctrl+C to exit.")

        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
