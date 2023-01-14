import threading
import requests


payloads = open('SQLI.txt', 'r').read().split('\n')

def test_sql_injection(url, payload):
    try:
        for u in url:
            al = f"{u}{payload}"
            r = requests.get(al)
            if "SQL" in r.text.upper() or "Error" in r.text.lower():
                print(f"[+] SQL Injection found: {al}")
                sqli = open('SQLI_result.txt', 'a')
                sqli.write(f"{al}\n")
                
    except Exception as e:
        print(e)

ur = input("Enter EndPoints Path >>> ")
url = open(ur, 'r').read().split('\n')
threads = []
for payload in payloads:
    t = threading.Thread(target=test_sql_injection, args=(url, payload))
    threads.append(t)
    t.start()


for t in threads:
    t.join()

