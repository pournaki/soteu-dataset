import os
import csv

raw_path = "txt/raw/"
speeches_path = "txt/nopreamble/"
speechfiles = os.listdir(speeches_path)
speechfiles = sorted([speeches_path + i for i in speechfiles])

## read the (meta)data
csvdicts = []
for doc_idx,path in enumerate(speechfiles):
    string = path.replace(speeches_path,"")
    date = string[:10]
    speaker = string[11:].replace(".txt","")
    ## get the text
    with open (path,"r") as f:
        text = f.read()  
    ## get the url
    with open (raw_path+string,"r") as f:
        for idx,line in enumerate(f.readlines()):
            if idx == 1:
                url = line[2:].replace("\n","")
                break
    csvdict = {'doc_id':doc_idx,
               'date':date,
               'speaker':speaker,
               'url':url,               
               'text':text}
    csvdicts.append(csvdict)
## write to csv
with open ("soteu_speeches.csv","w",encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=['doc_id','date','speaker','url','text'])
    writer.writeheader()
    for d in csvdicts:
        writer.writerow(d)
