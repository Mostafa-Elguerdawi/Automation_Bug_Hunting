import threading
import requests


payloads = open('Open_Redirect.txt', 'r').read().split('\n')

def test_open_redirect(url, payload):
    try:
        for u in url:
            al = f"{u}{payload}"
            r = requests.get(al)
            if r.status_code == 200:
                if r.url != url:
                    print(f"[+] Open Redirect found: {al}")
                    with open("open_redirect_results.txt", "a") as f:
                        f.write(f"{al}\n")
    except:
        pass


ur = input("Enter EndPoints Path >>> ")
url = open(ur, 'r').read().split('\n')
threads = []
for payload in payloads:
    t = threading.Thread(target=test_open_redirect, args=(url, payload))
    threads.append(t)
    t.start()


for t in threads:
    t.join()

