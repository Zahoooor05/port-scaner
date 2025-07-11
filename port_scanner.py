import socket
import sys

def scan_ports(host, ports):
    print(f"\n[INFO] Scanning {host}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"[+] Port {port} is open")
            sock.close()
        except KeyboardInterrupt:
            print("\n[!] Scan aborted by user.")
            sys.exit()
        except socket.error as e:
            print(f"[!] Could not connect to {host} on port {port} — {e}")
            continue

if __name__ == "__main__":
    try:
        target = input("Enter target IP or hostname: ").strip()
        socket.gethostbyname(target)  # Validate target resolves

        print("\nChoose scan type:")
        print("1. Common ports")
        print("2. Custom range")
        choice = input("Your choice (1 or 2): ")

        if choice == "1":
            ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 443, 8080]
        elif choice == "2":
            start_port = int(input("Start port: "))
            end_port = int(input("End port: "))
            ports_to_scan = list(range(start_port, end_port + 1))
        else:
            print("Invalid choice. Exiting.")
            sys.exit()

        scan_ports(target, ports_to_scan)

    except socket.gaierror:
        print("[ERROR] Hostname could not be resolved. Exiting.")
    except ValueError:
        print("[ERROR] Invalid port numbers. Exiting.")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")