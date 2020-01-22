"""Extracting PDFs from website"""

import sys
import requests

coll = sys.argv[1]

if coll == "bn":
    nrange = range(2037, 2103)
    base = "BiographieNationaleTome"
elif coll == "nbn":
    nrange = range(2103, 2120)
    base = "NouvelleBiographieNational"
else:
    print("Unknown collection")
    sys.exit()

for n in nrange:
    url = f"http://www.academieroyale.be/Academie/documents/FichierPDF{base}{n}.pdf"
    r = requests.get(url)
    if r.status_code == 200:
        with open(f"data/{coll}/{n}.pdf", "wb") as f:
            f.write(r.content)
    else:
        print(f"{n}: {r.status_code}")
