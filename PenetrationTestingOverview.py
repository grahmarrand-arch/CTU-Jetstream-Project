import socket
import requests

# -------------------------------
# 1. PORT SCANNER
# -------------------------------
def port_scan(target, ports):
    print(f"\n[+] Scanning ports on {target}...\n")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            else:
                print(f"[CLOSED] Port {port}")

            sock.close()
        except Exception as e:
            print(f"[ERROR] Port {port}: {e}")


# -------------------------------
# 2. HTTP SECURITY HEADERS CHECK
# -------------------------------
def check_headers(url):
    print(f"\n[+] Checking security headers for {url}...\n")

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        security_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Strict-Transport-Security",
            "Referrer-Policy",
            "Permissions-Policy"
        ]

        for header in security_headers:
            if header in headers:
                print(f"[OK] {header}")
            else:
                print(f"[MISSING] {header}")

    except Exception as e:
        print(f"[ERROR] {e}")


# -------------------------------
# 3. DIRECTORY SCANNER
# -------------------------------
def dir_scan(url):
    print(f"\n[+] Scanning for common directories on {url}...\n")

    paths = [
        "/admin",
        "/login",
        "/dashboard",
        "/backup",
        "/config",
        "/.env",
        "/test",
        "/api"
    ]

    for path in paths:
        full_url = url.rstrip("/") + path

        try:
            r = requests.get(full_url, timeout=3)

            if r.status_code == 200:
                print(f"[EXPOSED] {full_url}")
            elif r.status_code == 403:
                print(f"[FORBIDDEN] {full_url}")
            else:
                print(f"[NOT FOUND] {full_url}")

        except Exception:
            print(f"[ERROR] {full_url}")


# -------------------------------
# MAIN FUNCTION
# -------------------------------
def main():
    print("=== Basic Security Audit Tool ===")

    target = input("Enter target (IP or domain): ").strip()
    url = input("Enter full URL (e.g., https://example.com): ").strip()

    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]

    # Run all checks
    port_scan(target, common_ports)
    check_headers(url)
    dir_scan(url)

    print("\n[+] Scan completed.")


if __name__ == "__main__":
    main()