#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:15:18 2018

@author: saschajecklin
"""

import sys
import re
import pydeepl
from random import choice
from tqdm import tqdm

def make_xlat(*args, **kwds):
    adict = dict(*args, **kwds)
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    def xlat(text):
        return rx.sub(one_xlat, text)
    return xlat

if __name__ == "__main__":
    fileInputName = sys.argv[1]
    #fileInputName = "Introduction.tex"
    fileOutName = fileInputName.split('.')[0]+"_trans.tex"
    
    fileIn  = open(fileInputName, "r") 
    fileOut = open(fileOutName, "w")
    
    fileStr = fileIn.read()
    
    print("Starting hashing...")
     
    #replace commands like \begin{*}, \end{*}, tabs etc. with hashes
    searchObj1 = re.findall( r"\\begin\{\w+\}|\t|    |\r|\\end\{\w+\}|\\usepackage\{\w+\}|\\newcommand\{\w+\}|\\include\{.*\}|\\input\{\w+\}|\\\w+\[.*\}|\%.*", fileStr)
    #random number for every found command + a prefix which hopefully doens't appear in text. Used to skip lines later, which don't need translation
    list1 = ['X#X' + str(choice(range(1111, 9999, 1))) for x in searchObj1]
    #make a dictionary out of hashes
    d1 = dict(zip(searchObj1,list1))
    translate = make_xlat(d1)
    hashedText = translate(fileStr)
    
    # replace all latex commands (starting with a backslash) with hashes
    searchObj2 = re.findall( r"\\\w+",hashedText)
    #random number  + prefix again
    list2 = ['X#X' + str(choice(range(1111, 9999, 1))) for x in searchObj2]
    #make a dictionary
    d2 = dict(zip(searchObj2,list2))
    translate = make_xlat(d2)
    hashedText = translate(hashedText)
#    print(hashedText)
    #fileOut.write(translate(hashedText))
    
    d1.update(d2) # combine dictionaries
#    with open('hash_dict.json', 'w') as f:
#        json.dump(d1, f)
    
    print("Hashing done. Starting translation...")
    
    translated = ''
    for line in tqdm(hashedText.splitlines()): #tqdm is a progressbar
#        print(line)
        if line.startswith("X#X") and len(line) == 7:
            translated = translated + line + '\n'
            continue            
        if line == '\n':
            translated = translated + '\n'
        elif line == '':
            translated = translated + '\n'
        else: 
            translated = translated+pydeepl.translate(line, "DE", "EN")+'\n'
#    translated = translated+pydeepl.translate(hashedText, "DE", "EN")
#    print(translated)
    
    d1Inv = {val:key for (key, val) in d1.items()} #swap dictionary
    translate2 = make_xlat(d1Inv)
    fileStrOut = translate2(translated)
#    print(fileStrOut)
    
    fileOut.write(fileStrOut)
        
    print("success")
    fileIn.close()
    fileOut.close()