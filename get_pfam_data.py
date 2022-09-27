#------------------------------------------------------------------------
#Get_pfam_data
#Source: https://github.com/rplemos/get_pfam_data
#Author: Rafael Lemos
#------------------------------------------------------------------------


#Libraries

import pfam
#from beeprint import pp
import sys
import requests


#Parsing input

try:   
    input = (sys.argv[1])
    type = (sys.argv[2]).lower()
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <FamilyName> <Alignment Type>")


#Getting HMM, aligment and family information
    
fam = pfam.family(input)
url_hmm = 'http://pfam.xfam.org/family/' + input + '/hmm'
url_align = 'http://pfam.xfam.org/family/' + input + '/alignment/' + type


#Displaying family description and preparing protein list for output

protein_list = fam.proteins()
print (f"\nFamily Description: \n {fam.comment}\n")


#Writing sequences file in .fasta format

cont = 0
with open (r"sequences_{input}.txt","w") as fp:
    for i in protein_list:        
        fp.write (f">{protein_list[cont].id}")
        fp.write ("\n")
        protein = protein_list[cont].fetch()
        fp.write (protein.sequence)
        fp.write ("\n")
        cont = cont + 1
fp.close()


#Writing HMM and aligment files

response_hmm = requests.get(url_hmm)
with open (f"hmm_{input}.hmm","w") as fp:
    fp.write(response_hmm.text)
fp.close()

response_align = requests.get(url_align)
with open (f"alignment_{input}_{type}.txt","w") as fp:
    fp.write(response_align.text)
fp.close()
