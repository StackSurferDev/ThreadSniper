import socket
from concurrent.futures import ThreadPoolExecutor
import time

open_ports = []

def scan_port(ip, port):
    """Try to connect to a single port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"🟢 Port {port} is OPEN")
                open_ports.append(port)
    except Exception:
        pass

def main():
    print("🔍 Threaded Port Scanner (0–65535 ports)")
    target_ip = input("Enter target IP (e.g. 127.0.0.1): ")

    start = time.time()
    print(f"\nStarting scan on {target_ip}...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(0, 65536):
            executor.submit(scan_port, target_ip, port)

    end = time.time()
    print(f"\n✅ Scan completed in {round(end - start, 2)} seconds.")
    print(f"Open ports found: {sorted(open_ports) if open_ports else 'None'}")

if __name__ == "__main__":
    main()
