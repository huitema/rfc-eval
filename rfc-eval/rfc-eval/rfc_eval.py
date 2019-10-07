
#!/usr/bin/python
# coding=utf-8
#
import sys
import codecs
import urllib.request as request
import json

def getRfcRef(rfc):
    url = "http://api.semanticscholar.org/v1/paper/10.17487/rfc" + rfc + "?include_unknown_references=true"
    with request.urlopen(url) as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print("error for <" + url + ">")
            data = []
    return data

def countCitations(data, year, influential):
    nb_citations = 0
    if 'citations' in data:
        for citation in data['citations']:
            if year == 0 or ('year' in citation and citation['year'] == year):
                if not influential or ('isInfluential' in citation and citation['isInfluential'] == True):
                    nb_citations += 1
    return nb_citations

def tableLine (rfc, status, year, refYear):
    data = getRfcRef(rfc)
    n_o = countCitations(data, 0, False)
    n_y = countCitations(data, year, False) + countCitations(data, year+1, False)
    n_r = n_y
    if year != refYear:
        n_r = countCitations(data, refYear, False) + countCitations(data, refYear+1, False)
        print(rfc + "|" + status + "|" + str(n_o) + "|" + str(n_y) + "|" + str(n_r))
    else:
        print(rfc + "|" + status + "|" + str(n_o) + "|" + str(n_y))

def table(rfc_list, year, refYear):
    print("")
    if year != refYear:
        print("RFC(" + str(year) + ") | Status | Total | " + str(year) + "-" + str(year+1) + " | " + str(refYear) + "-" + str(refYear+1))
        print("---- | ---- | ----:| ----:| ----:")
    else:
        print("RFC(" + str(year) + ") | Status | Total | " + str(year) + "-" + str(year+1) )
        print("---- | ---- | ----:| ----:")
    for rfc_line in rfc_list:
        tableLine(rfc_line[0], rfc_line[1], year, refYear)


# Obtain the reference and print the corresponding table in MD format.

rfc_2018 = [["8411","Info"],
["8456","Info"],
["8446","PS"],
["8355","Info"],
["8441","PS"],
["8324","ISE"],
["8377","PS"],
["8498","Info"],
["8479","ISE"],
["8453","Info"],
["8429","BCP"],
["8312","Info"],
["8492","ISE"],
["8378","Exp"],
["8361","PS"],
["8472","PS"],
["8466","PS"],
["8362","PS"],
["8468","Info"]]

rfc_2008 = [["5326","Exp"],
["5348","PS"],
["5281","Info"],
["5354","Exp"],
["5227","PS"],
["5329","PS"],
["5277","PS"],
["5236","ISE"],
["5358","BCP"],
["5271","Info"],
["5195","PS"],
["5283","PS"],
["5186","Info"],
["5142","PS"],
["5373","PS"],
["5404","PS"],
["5172","PS"],
["5349","Info"],
["5301","PS"],
["5174","Info"]]

rfc_1998 = [["2289","PS"],
["2267","Info"],
["2317","BCP"],
["2404","PS"],
["2374","PS"],
["2449","PS"],
["2283","PS"],
["2394","Info"],
["2348","DS"],
["2382","Info"],
["2297","ISE"],
["2381","PS"],
["2312","Info"],
["2387","PS"],
["2398","Info"],
["2391","PS"],
["2431","PS"],
["2282","Info"],
["2323","ISE"],
["2448","ISE"]]

table(rfc_2018, 2018, 2018)
table(rfc_2008, 2008, 2018)
table(rfc_1998, 1998, 2018)


