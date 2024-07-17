# port_scanner.py
import socket
from threading import Thread, Lock

# Define global print lock
print_lock = Lock()

# Define global file lock
file_lock = Lock()

def scan_port(ip, port, output_file):
    """
    Scans a single port on a given IP address and writes the result to a file.

    Parameters:
    ip (str): The IP address to scan.
    port (int): The port to scan.
    output_file (str): The file to write the scan results to.

    Returns:
    None
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout
        sock.settimeout(1)
        # Attempt to connect to the port
        result = sock.connect_ex((ip, port))
        # If the result is 0, the port is open
        if result == 0:
            with print_lock:
                print(f"Port {port} is open on {ip}")
            with file_lock:
                with open(output_file, 'a') as file:
                    file.write(f"Port {port} is open on {ip}\n")
        # Close the socket
        sock.close()
    except socket.error as err:
        with print_lock:
            print(f"Error scanning port {port} on {ip}: {err}")

def scan_ports(ip, start_port, end_port, output_file):
    """
    Scans a range of ports on a given IP address and writes the results to a file.

    Parameters:
    ip (str): The IP address to scan.
    start_port (int): The starting port number.
    end_port (int): The ending port number.
    output_file (str): The file to write the scan results to.

    Returns:
    None
    """
    print(f"Scanning ports {start_port}-{end_port} on {ip}...")
    threads = []
    for port in range(start_port, end_port + 1):
        thread = Thread(target=scan_port, args=(ip, port, output_file))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print(f"Scanning complete. Results are saved in {output_file}")

def main():
    """
    Main function to execute the port scanner script.
    """
    ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    output_file = "scan_results.txt"
    
    # Clear the output file before starting the scan
    with open(output_file, 'w') as file:
        file.write(f"Port scan results for {ip} (Ports {start_port} to {end_port}):\n\n")
    
    scan_ports(ip, start_port, end_port, output_file)

if __name__ == "__main__":
    main()
