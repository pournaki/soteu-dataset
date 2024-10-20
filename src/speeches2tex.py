import os

tex_preamble = """\\documentclass[a4paper,11pt]{article}
\\setlength{\\parindent}{0cm}
\\usepackage[margin=1in]{geometry}
\\usepackage{eurosym}
\\usepackage{titlesec}
\\title{State of the European Union Speeches}
\\date{}
\\titleformat*{\\section}{\\normalsize\\bfseries}
\\usepackage{hyperref}
\\usepackage{url}
\\hypersetup{
    colorlinks,
    citecolor=black,
    filecolor=black,
    linkcolor=black,
    urlcolor=black
}
\\begin{document}
\\maketitle
\\tableofcontents
\\newpage\n
"""

tex_postamble = """
\\end{document}
"""

tex_body = ""

raw_path = "txt/raw/"
speeches_path = "txt/nopreamble/"
speechfiles = os.listdir(speeches_path)
speechfiles = sorted([speeches_path + i for i in speechfiles])

for doc_idx,path in enumerate(speechfiles):
    string = path.replace(speeches_path,"")
    date = string[:10]
    speaker = string[11:].replace(".txt","").replace("_"," ")
    ## get the text
    with open (path,"r") as f:
        text = f.read()
    with open (raw_path+string,"r") as f:
        for idx,line in enumerate(f.readlines()):
            if idx == 1:
                url = line[2:].replace("\n","")
                break        
    sectionstring = f"\\section{{Speech {doc_idx+1} - {speaker} - {date}}}\n"        
    tex_body += sectionstring
    tex_body += f"\\url{{{url}}}\\\\[3mm]\n"
    tex_body += text.replace("%","\\%").replace("&","\\&").replace("€","\\euro")
    tex_body += "\n \\newpage"

write = tex_preamble + tex_body + tex_postamble    

with open ("tex/soteu_speeches.tex","w",encoding="utf-8") as f:
    f.write(write)
