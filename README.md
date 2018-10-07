# texTrans
Translates LaTex Files with DeepL
Credits for the Python DeepL Wrapper "pydeepl" go to EmilioK97. The cool progress-bar comes from the tqdm developers.

This project is currently in its alpha state. It works but is still a mess. Sadly DeepL has a problem accepting longer texts with many hashes (used e.g. for newline and tabs). Therefor the translation is carried out line by line, which obviously takes some time.

Prerequisites
------------

    pip install pydeepl
    pip install tqdm
    
Usage
------------

    python textTrans <input File>
Output will be created as input_trans.tex
    
    
