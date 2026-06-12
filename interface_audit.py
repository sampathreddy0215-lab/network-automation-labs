from netmiko import ConnectHandler
import csv

devices = [
    {
        "device_type": "cisco_ios",
        "host": "10.1.1.1",
        "username": "admin",
        "password": "password"
    }
]

with open("interface_audit_report.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([
        "Device",
        "Interface",
        "IP Address",
        "Status",
        "Protocol"
    ])

    for device in devices:

        connection = ConnectHandler(**device)

        output = connection.send_command(
            "show ip interface brief"
        )

        lines = output.splitlines()[1:]

        for line in lines:

            columns = line.split()

            if len(columns) >= 6:

                writer.writerow([
                    device["host"],
                    columns[0],
                    columns[1],
                    columns[4],
                    columns[5]
                ])

        connection.disconnect()

print("Interface audit completed.")
