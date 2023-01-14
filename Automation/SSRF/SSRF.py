import threading
import requests

urls = ['', '']

def test_ssrf(url, test_url):
    try:
        for u in url:
            al = f"{u}{payload}"
            r = requests.get(al)
            if r.status_code == 200:
                print(f"[+] SSRF found: {al}")
                ssrf = open('SSRF_results.txt', 'a')
                ssrf.write(f"{al}\n")
            
    except Exception as e:
        print(e)


ur = input("Enter EndPoints Path >>> ")
url = open(ur, 'r').read().split('\n')
threads = []
for test_url in urls:
    t = threading.Thread(target=test_ssrf, args=(url, test_url))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

