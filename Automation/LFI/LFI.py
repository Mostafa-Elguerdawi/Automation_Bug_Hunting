import requests
import threading

payloads = open('/home/melguerdawi/Desktop/Pentest/Web/hunt/Automation/LFI/LFI.txt', 'r').read().split('\n')

def test_lfi(url, payload):
    for u in url:
        al = f"{u}{payload}"
        payload_response = requests.get(al)
        normal_response = requests.get(al)
    
        if len(payload_response.text) > len(normal_response.text):
            print(f"LFI vulnerability found with payload: {al}")
            lfi = open('/home/melguerdawi/Desktop/Pentest/Web/hunt/Automation/LFI/LFI_results.txt', 'a')
            f.write(f"{al}\n")


ur = input("Enter EndPoints Path >>> ")
url = open(ur, 'r').read().split('\n')
threads = []
for payload in payloads:
    t = threading.Thread(target=test_lfi, args=(url, payload))
    threads.append(t)
    t.start()
for t in threads:
    t.join()



