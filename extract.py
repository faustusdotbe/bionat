"""Extracting PDFs from website"""

import sys
import requests
from tqdm import tqdm
import os

coll = sys.argv[1]


def download(coll,nrange,base):
	print("Downloading",coll)
	for n in tqdm(nrange):
		url = f"http://www.academieroyale.be/Academie/documents/FichierPDF{base}{n}.pdf"
		r = requests.get(url)
		if os.path.exists(f"data/{coll}") == False:
			os.mkdir(f"data/{coll}")
		if r.status_code == 200:
			with open(f"data/{coll}/{n}.pdf", "wb") as f:
				f.write(r.content)
		else:
			print(f"{n}: {r.status_code}")

	if coll == "nbn": # handle extra file
		url = "https://www.academieroyale.be/Academie/documents/ALBIMOORWilly18211.pdf"
		r = requests.get(url)
		with open(f"data/nbn/2112.pdf", "wb") as f:
			f.write(r.content)

if coll == "bn":
	nrange = range(2037, 2103)
	base = "BiographieNationaleTome"
	download(coll,nrange,base)
	
elif coll == "nbn":
	nrange = range(2103, 2112)
	base = "NouvelleBiographieNational"
	download(coll,nrange,base)
	
elif coll == "all":
	coll = "bn"
	nrange = range(2037, 2103)
	base = "BiographieNationaleTome"
	download(coll,nrange,base)
	
	coll = "nbn"
	base = "NouvelleBiographieNational"
	download(coll,nrange,base)

	
else:
	print("Unknown collection")
	sys.exit()

