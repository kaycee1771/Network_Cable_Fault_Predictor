import requests

DEVICES = [
    {"name": "switch_1", "interfaces": ["eth1", "eth2"]}
]

def poll_all():
    for device in DEVICES:
        for iface in device["interfaces"]:
            try:
                response = requests.get("http://localhost:8000")
                snmp = response.json()
                print({
                    "device": device["name"],
                    "interface": iface,
                    "in_octets": snmp["in_octets"],
                    "out_octets": snmp["out_octets"],
                    "in_errors": snmp["in_errors"],
                    "out_errors": snmp["out_errors"],
                    "speed": snmp["speed"]
                })
            except Exception as e:
                print(f"[ERROR] {device['name']}:{iface} - {e}")

if __name__ == "__main__":
    poll_all()
