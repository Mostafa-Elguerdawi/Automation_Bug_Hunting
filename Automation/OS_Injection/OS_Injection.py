import threading
import requests


payloads = open('OS.txt', 'r').read().split('\n')

def test_os_cmd_injection(url, payload):
    try:
        for u in url:
            al = f"{u}{payload}"
            r = requests.get(al)
            if "uid" in r.text or "root" in r.text or "list" in r.text or "-rw" in r.text or "www-data" in r.text or "passwd" in r.text or "Local Address" in req.text or "System" in r.text or "C:" in r.text or "apache" in req.text:
                print(f"[+] OS Command Injection found: {url}{payload}")
                with open("os_cmd_injection_results.txt", "a") as f:
                    f.write(f"{al}\n")
    except:
        pass


ur = input("Enter EndPoints Path >>> ")
url = open('ur', 'r').read().split('\n')
threads = []
for payload in payloads:
    t = threading.Thread(target=test_os_cmd_injection, args=(url, payload))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


