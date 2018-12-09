#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:15:18 2018

@author: saschajecklin
"""
import re
import pydeepl
import argparse
import time
from tqdm import tqdm

def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Translates LaTeX files with DeepL')
    parser.add_argument("-f", dest="FROM", default="DE", required=True, help="Language of the source document(s) e.g. DE")
    parser.add_argument("-t", dest="TO", default="EN", required=True, help="Language of the target document e.g EN")
    parser.add_argument("-i", dest="FILENAME", required=True, nargs="+", help="Path(s) to the latex file(s)")
    return parser.parse_args(args)

def make_xlat(*args, **kwds):
    adict = dict(*args, **kwds)
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    def xlat(text):
        return rx.sub(one_xlat, text)
    return xlat

def translate(text: str, lang_in="DE", lang_out="EN"):
    translated = []
    commands = (r"^@#X\d{18,19}$", # if it starts with @#X followed by 18 to 19 digits its just a hash --> no translation needed
                r"^@#X-\d{18,19}$")
    only_hash_pattern = re.compile("|".join(commands))
    for line in text.splitlines():
        #print(line)
        if line in {'', '\n'} or only_hash_pattern.match(line):
            translated.append(line)
#        elif not line.strip():
#            translated.append('')
        else:
            translated.append(pydeepl.translate(line, lang_in, lang_out))
            time.sleep(0.6) #problem with to many requests. not yet solved
    translated = '\n'.join(translated)
    return translated

if __name__ == "__main__":
    args = parse_args()
    print('Translating file {} to {} from {}'.format(*args.FILENAME, args.TO, args.FROM))
    fileInputName = args.FILENAME[0]
    #fileInputName = "Introduction.tex"
    fileOutName = fileInputName.split('.')[0] + "_trans.tex"

    with open(fileInputName) as fileIn, open(fileOutName, "w") as fileOut:

        fileStr = fileIn.read()
    
        print("Starting hashing...")
    
        #replace commands like \begin{*}, \end{*}, tabs etc. with hashes
        search_pattern = (
            r"\\begin\{\w+\}",
            r"\t",
            "    ",
            "\r",
            r"\\end\{\w+\}",
            r"\\usepackage\{\w+\}",
            r"\\newcommand\{\w+\}",
            r"\\include\{.*\}",
            r"\\input\{\w+\}",
            r"\\\w+\[.*\}",
            r"\%.*",
        )
        search_result_1 = re.findall("|".join(search_pattern), fileStr)
        # random number for every found command + a prefix which hopefully 
        # doens't appear in text. Used to skip lines later, which don't need translation
        list1 = ['@#X{}'.format(hash(x)) for x in search_result_1]
        #make a dictionary out of hashes
        d1 = dict(zip(search_result_1, list1))
        hash_dictionary = make_xlat(d1)
        hashedText = hash_dictionary(fileStr)
    
        #replace all latex commands (starting with a backslash) with hashes
        search_result_2 = re.findall( r"\\\w+", hashedText)
        #random number  + prefix again
        list2 = ['@#X{}'.format(hash(x)) for x in search_result_2]
        #make a dictionary
        d2 = dict(zip(search_result_2, list2))
        hash_dictionary = make_xlat(d2)
        hashedText = hash_dictionary(hashedText)
        #print(hashedText)
        #fileOut.write(translate(hashedText))
    
        d1.update(d2) # combine dictionaries
        #with open('hash_dict.json', 'w') as f:
        #json.dump(d1, f)
    
        print("Hashing done. Starting translation...")

        translated = translate(text=hashedText, lang_in = args.FROM, lang_out = args.TO)
    
        d1Inv = {val:key for (key, val) in d1.items()} #swap dictionary
        translate2 = make_xlat(d1Inv)
        fileStrOut = translate2(translated)
        #print(fileStrOut)
    
        fileOut.write(fileStrOut)
    
        print("Success")