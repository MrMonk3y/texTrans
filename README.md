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

    python textTrans.py -f <FROM> -t <TO> -i <input File>
    
    Example:
    python texTrans.py -f DE -t EN - myfile.tex
Output will be created as input_trans.tex

ToDo
----
DeepL changed their API which causes problems sending the text

- [ ] Fix pydeepl API or use something else


Disclaimer
----------
Using this script could violate the ToS of DeepL. Therefore the purpose of this script is purely educational. Furthermore, the translation API can easily be switched to another API.
    
    
