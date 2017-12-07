
from urllib.request import urlopen, Request, URLError, HTTPError
urls = ['https://www.digikey.com/products/en?keywords=RC0805JR-071KL',
'https://www.digikey.com/products/en?keywords=08055C333KAT2A',
'https://www.digikey.com/products/en?keywords=B72660M0251K072',
'https://www.digikey.com/products/en?keywords=HI1206T500R-10',
'https://www.digikey.com/products/en?keywords=LVR005NK-2',
'https://www.digikey.com/products/en?keywords=RL1220S-120-F',
'https://www.digikey.com/products/en?keywords=RMCF0805JT330R',
#'https://www.digikey.com/scripts/DkSearch/dksus.dll?WT.z_header=search_go&lang=en&keywords=IND-LED',
'https://www.digikey.com/products/en?keywords=CHV1206-JW-224ELF',
'https://www.digikey.com/products/en?keywords=RAC03-3.3SGA',
'https://www.digikey.com/products/en?keywords=202R18W102KV4E',
'https://www.digikey.com/products/en?keywords=GRM32DR72H104KW10L']
# 'https://www.digikey.com/scripts/DkSearch/dksus.dll?WT.z_header=search_go&lang=en&keywords=CRE1S0505S3C',
# 'https://www.digikey.com/scripts/DkSearch/dksus.dll?WT.z_header=search_go&lang=en&keywords=SJ-3523-SMT-TR',
# 'https://www.digikey.com/scripts/DkSearch/dksus.dll?WT.z_header=search_go&lang=en&keywords=ATM90E26-YU-RCT-ND',
# 'https://www.digikey.com/scripts/DkSearch/dksus.dll?WT.z_header=search_go&lang=en&keywords=CL21F104ZBCNNNC',
# 'https://www.digikey.com/scripts/DkSearch/dksus.dll?WT.z_header=search_go&lang=en&keywords=CL21A106KQCLRNC',
# 'https://www.digikey.com/scripts/DkSearch/dksus.dll?WT.z_header=search_go&lang=en&keywords=535-9865-1-ND',
# 'https://www.digikey.com/scripts/DkSearch/dksus.dll?WT.z_header=search_go&lang=en&keywords=c',
# 'https://www.digikey.com/scripts/DkSearch/dksus.dll?WT.z_header=search_go&lang=en&keywords=CL21C180JBANNNC',
# 'https://www.digikey.com/scripts/DkSearch/dksus.dll?WT.z_header=search_go&lang=en&keywords=BLM15AG100SN1D',
# 'https://www.digikey.com/scripts/DkSearch/dksus.dll?WT.z_header=search_go&lang=en&keywords=RMCF0805JT51R0',
# 'https://www.digikey.com/scripts/DkSearch/dksus.dll?WT.z_header=search_go&lang=en&keywords=SI8651BB-B-IS1']
#####################################
import random
def FakeBrowser(url):
    userAgentStrings = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1',
    'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
    'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36']


    req = Request(url)
    req.add_header('Accept-Language', 'en-US')
    req.add_header('User-agent', random.choice(userAgentStrings) )

    return req
##########################################################
counter = 1
for url in urls:
    print(url)
    numTries = 0
    while True:
        try:
            req = FakeBrowser(url)
            with urlopen(req) as response:
                html = response.read()
                print (html)
            print(counter,"DONE WITH THIS URL.")
            counter += 1
            break
        except HTTPError as e:
            print(e.reason)
            print(e.code)
            if (e.code == 403 and numTries < 10):
                numTries += 1
                continue
            else:
                print("BYE...NUMTRIES: ",numTries)
                break
