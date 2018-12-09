#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 13:16:27 2018

@author: saschajecklin
"""

import re
from random import choice
import pydeepl

def rmFormat(text):
    searchObj1 = re.findall( r"X\w+", text)
    if searchObj1 == []:
        return text
    
    listRegex = [r'#' + str(choice(range(1111, 9999, 1))) for x in searchObj1]
    #make a dictionary
    d1 = dict(zip(searchObj1,listRegex))
    translate = make_xlat(d1)
    hashedText = translate(text)
    print(hashedText)    
    translated = pydeepl.translate(hashedText, "DE", "EN")
    
    d1Inv = {val:key for (key, val) in d1.items()} #swap dictionary
    translate2 = make_xlat(d1Inv)
    return translate2(translated)
    

    
    
    
def make_xlat(*args, **kwds):
    adict = dict(*args, **kwds)
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    def xlat(text):
        return rx.sub(one_xlat, text)
    return xlat


if __name__ == "__main__":
    text = r'''X6851X7483X8947{Introduction}X7483X9772{Why Law?}X7483X6845X7483X6259X6992 social framework X7483X6259X6992 conflict managementX7483X6259X6992 preserve valuesX7483X6259X6992 social framework for integrationX7483X6259X6992 legitimate public authorities and courtsX7483X6259X6992 control of powerX7483X6259X6992 forces each to express his will carefullyX7483X4106X7483X7483X9772{The importance of law in a technical world}X7483X6845X7483X6259X6992 Law as framework/guideline of the allowed (= maximum) or the obligatory requirement (= minimum) of a systemX7483X6259X6992 Clarifying of obligations and responsibility/liabilityX7483X6259X6992 Industry standards complete the lawX7483X6259X6992 But (technical) standards often doesn't clear all legal question (cloud-contracts, IoT, ...)X7483X4106X7483X7483X9772{Law as risk management}X7483X6845X7483X6259X6992 To handle risks it's reasonable to take technical („security by design“), organizational and legal measures.X7483X6259X6992 Legal support is necessary as early as possible! Otherwise projects might be „shot off“ in the very last minute!X7483X6259X6992 By law the management is personally responsible to organize and control the legal compliance! X7483X4106X7483X7483X9772{One of the most vital legal question}X7483$X4578{1}{X6807{X8512{WHO}}}$ wants from $ X4578{2}{X6807{X8512{WHOM} }} X4578{3}{X6807{X8512{WHAT} }}$ based on what $X4578{4}{X6807{X8512{TITLE}}}$ (right)?X7483X7483X9772{Correct legal argumentation}X7483A statement/claim has to be justified by legal articles/arguments and the essential evidence or based on legal articles/arguments and with the essential evidence you get to a conclusion.X7483X7483X9772{Conventions, moral and law}X7483X2709X7483X7483X9772{Law under different perspectives}X7483Classification is based upon:X7483X6845X7483X6259X6992 status (constitution, act, regulations/by-law)X7483X6259X6992 issuer (federal-, cantonal- and communal law)X7483X6259X6992 source of law (written law, common law, judicial tradition)X7483X6259X6992 involved person (civil law or public law)X7483X4106X7483X7483X9772{Separation of Powers}X7483X6845X7483X6259X6992 „Das Schweizervolk und die Kantone bilden die Schweizerische Eidgenossenschaft“ (Art. 1 BV) – not vice-versa!X7483X6259X6992 „Der Kanton arbeitet mit den Gemeinden, den anderen Kantonen, dem Bund und, in seinem Zuständigkeitsbereich, mit dem Ausland zusammen.“ (§ 4 Kantonsverfassung ZH)X7483X6259X6992 The State is only entitled to legislate and to act in a territory/legal field if he has a constitutional legitimation!X7483X6259X6992 Cantons are in their power of legislation superior to the State!X7483X4106X7483X7483X9772{Civil and Public Law}X7483X6845X7483X6259X6992 Civil law is mastered by the principle of freedom of coalition and freedom of contract.X7483X6259X6992 Public law is mastered by the principle of legality (control of power).X7483X6259X6992 This results into completely different jurisdiction (civil-/criminal-X6259or administrative court) with each different procedures and rights.X7483X4106X7483X7483X9772{by-law (Verordnung) and order (Verfügung)}X7483X6845X7483X6259X6992 By-Law is a general, abstract regulation as part of a law.X7483X6259X6992 An Order is an individual, concrete application of law to a person (i.e. monetary fine for parking too long or aX7483X6259building permit).X7483X4106X7483X7483X9772{Switzerland and foreign countries}X7483X6845X7483X6259X6992 We're integrated into a longtime European legal tradition and uni-/bilateral conventions.X7483X6259X6992 We have a long history in commercial relationship with other countries.X7483X6259X6992 The IPRG (Gesetz über das internationale Privatrecht) is our „gateway“ between swiss and foreign law.X7483X6259X6992 IPRG rules, which law (swiss or foreign) is applicable and which (swiss or foreign) court is competent.X7483X6259X6992 Parties can (in most cases) decide under which jurisdiction they want to handle their disputes and which court will be competent.X7483X4106'''
    print(rmFormat(text))