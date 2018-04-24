import pandas as pd
import subprocess
from collections import namedtuple
from PyPDF2 import PdfFileMerger
import os
import functools

df = pd.read_csv('applicants.csv')

#custom comparator for ranking applicants during generation phase
#First by Major, then by Year, then by Name
def compare(item1, item2):
    if item1[1] < item2[1]:
        return -1
    elif item1[1] > item2[1]:
        return 1
    if item1[2] > item2[2]:
        return -1
    elif item1[2] < item2[2]:
        return 1
    if item1[0] < item2[0]:
        return -1
    elif item1[0] > item2[0]:
        return 1
    return 0

companies = {}

#parse google form data into data structures
for index, row in df.iterrows():
    comps = row['What companies are you interested in?'].split(", ")
    for c in comps:
        end = c.find('(')
        ctemp = c[:end-1]
        if ctemp == "Oath/Yahoo!":
            ctemp = "Oath-Yahoo!"
        if ctemp not in companies:
            companies[ctemp] = []
        year = 0
        if (row['What year are you?'] == "Freshman"):
                year = 1 
        if (row['What year are you?'] == "Sophomore"):
                year = 2
        if (row['What year are you?'] == "Junior"):
                year = 3
        if (row['What year are you?'] == "Senior"):
                year = 4
        if (row['What year are you?'] == "Graduate"):
                year = 5
        companies[ctemp].append((row['What is your name? (Firstname Lastname)'], row['What is your major?'], year))

event = input("At what event did Theta Tau work with these companies? ")

#generate cover pages!
for c, p in companies.items():
    p = sorted(p, key=functools.cmp_to_key(compare))
    #sorted(p, key = operator.itemgetter(2, 1, 3))
    filename = c + ".tex"
    f = open(filename,"w")
    f.write('\\documentclass[10pt,stdletternofrom,dateyes,sigleft]{newlfm}\n')
    f.write('\\usepackage{charter}\n')
    f.write('\\newsavebox{\\Luiuc}\sbox{\\Luiuc}{\parbox[b]{1.75in}{\\vspace{0.5in}\n')
    f.write('\\includegraphics[width=1.2\\linewidth]{logo.png}}}\n')
    f.write('\\makeletterhead{Uiuc}{\\Lheader{\\usebox{\\Luiuc}}}\n')
    f.write('\\lthUiuc\n')

    f.write('\\greetto{Dear ' + c + ' Recruiting Team,}')

    f.write('\\begin{document}\n')
    f.write('\\begin{newlfm}\n')

    f.write("We've enjoyed working with " + c + " this semester organizing this " + event + ", and we ")
    f.write("hope we were able to provide a great experience for your team. We're proud to partner with you ")
    f.write("and look forward to working with you on campus again!\\\\")
    f.write("\\\\")
    f.write("Our organization is made up of engineers from all majors throughout the College of Engineering with a diverse ")
    f.write("set of experiences and backgrounds. We would like to share the resumes of our members who are specifically ")
    f.write("interested in opportunities with " + c + ". We have organized this resume book based on major, then seniority, ")
    f.write("then alphabetically by last name.\\\\")
    f.write("\\\\")

    tempMaj = p[0][1]
    f.write("\\textbf{" + tempMaj + ":}\\\\\n")
    for per in p:
        if per[1] != tempMaj:
            tempMaj = per[1]
            f.write("\\textbf{" + tempMaj + ":}\\\\\n")
        f.write(per[0] + "\\\\\n")

    f.write('\\end{newlfm}\n')
    f.write('\\end{document}\n')

    f.close()

    cmd = ['pdflatex', '-interaction', 'nonstopmode', filename]
    proc = subprocess.Popen(cmd)
    proc.communicate()
    #filename = "/home/josh/School/thetaTau/resumeBook/" + c + ".pdf"
    filename = c + ".pdf"
    cmd = ['mv', filename, './coverLetters']
    proc = subprocess.Popen(cmd)
    proc.communicate()


#merge pdfs!
for c, p in companies.items():

    p = sorted(p, key=functools.cmp_to_key(compare))
    original = './coverLetters/' + c + '.pdf'
    pdfs = [original]
    merger = PdfFileMerger()
    tempMaj = "SRI"
    for per in p:
        if per[1] != tempMaj:
            tempMaj = per[1]
            filename = tempMaj + ".tex"
            f = open(filename,"w")
            f.write('\\documentclass{article}\n\\usepackage{soul}\n')
            f.write('\\begin{document}\n\\begin{center}\n\\large\\bfseries\n')
            f.write('\\ul{' + tempMaj + '}\n')
            f.write('\\end{center}\n\\end{document}\n')
            f.close()
            cmd = ['pdflatex', '-interaction', 'nonstopmode', filename]
            proc = subprocess.Popen(cmd)
            proc.communicate()
            filename = "./" + tempMaj + ".pdf"
            pdfs.append(filename)
        tempName = per[0].replace(' ', '_')
        resName = './resumes/' + tempName + '_Resume.pdf'
        pdfs.append(resName)
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(open(pdf, 'rb'))
    new = './books/' + c + '.pdf'
    with open(new, 'wb') as fout:
        merger.write(fout)

