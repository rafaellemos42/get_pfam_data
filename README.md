# get_pfam_data
Simple code to get PFAM (Protein Family Database) data directly from the website API

For usage, `pfam` library is necessary. To install, please refer to:
>https://github.com/AlbertoBoldrini/python-pfam

The `beeprint` package is also necessary for some data visualization (not mandatory).

## Example:
```
python3 get_pfam_data family_name alignment_type
```
Arguments: 
- **family_name:** PFxxxxx, where x is the number of the family
- **aligment_type:** can be: "seed", "full", "rp15", "rp35", "rp55", "rp75", or "uniprot". For more details, please refer to the PFAM website.
