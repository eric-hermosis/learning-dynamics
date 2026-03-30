from luthor.latex import Command, Document
from luthor.compiler import Compiler 

document = Document(
    preamble=[
        Command("documentclass", ["12pt"], {"article"}), 
        Command("usepackage", ["utf8"], {"inputenc"}),
        Command("usepackage", ["T1"], {"fontenc"}), 
        Command("usepackage", {"lmodern"}),
        Command("usepackage", {"amsmath"}),
        Command("usepackage", {"amssymb"}),
        Command("usepackage", {"hyperref"}),
        Command("usepackage", {"cite"}),
        Command("usepackage", {"graphicx"}), 
        Command("usepackage", {"longtable"}),
        Command("usepackage", {"booktabs"}), 
        Command("usepackage", ["font=small","labelfont=bf","margin=0.5cm"], {"caption"}),
        Command("usepackage", ["paper=a4paper", "top=3.5cm", "bottom=3.5cm", "left=3.5cm", "right=3.5cm"], {"geometry"}), 
        Command("setlength", {"\\parindent"}, {"0pt"}),
        Command("setlength", {"\\parskip"}, {"1em"}),
        Command("setcounter", {"secnumdepth"}, {"0"}),
        Command("title", {"Learning Dynamics"}),
        Command("author", {"Eric Hermosis"}),
        Command("date", {"\\today"}),  
    ],

    body=[ 
        Command("maketitle"),
        Command("begin", {"abstract"}),
        Command("input", {"abstract"}),
        Command("end", {"abstract"}),
        Command("input", {"index"}),
        Command("bibliographystyle", {"unsrt"}),
        Command("bibliography", {"references"}),
        Command("include", {"appendix"}),  
    ]
) 

import shutil
import os

if __name__ == "__main__": 
    compiler = Compiler("article")
    compiler.compile(document)

    src = os.path.join("build", "article.pdf")
    dst = "article.pdf" 
    shutil.copy(src, dst) 