# monitor-bluetooth-data-on-windows
Connect your Bluetooth/BLE device to your Windows PC and run this python script to see your sensor data. 

This Python utility allows you to connect to a Bluetooth Low Energy (BLE) device from a Windows machine and monitor live sensor data over GATT. It is especially useful when you need to validate or debug a Bluetooth application but do not have immediate access to a Linux environment. To adapt it for your application, simply update the device name and UUIDs.

In my regular workflow, I typically use bluetoothctl on Linux to test and validate Bluetooth firmware. Linux provides excellent low-level visibility and control over BLE interactions. However, during a recent situation where I only had access to a Windows machine, I researched for a Python workaround and found that the Bleak library.

Feel free to contact me for any support, suggestions or improvements.
