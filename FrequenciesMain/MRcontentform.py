f = open('MRcontentform.txt','w+')

#This produces code for calculating frequencies for reading variables


f.write("""USE ALL.
COMPUTE filter_$=(pro = 0).
VARIABLE LABELS filter_$ 'pro = 0 (FILTER)'.
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'.
FORMATS filter_$ (f1.0).
FILTER BY filter_$.
EXECUTE.

""")

switchtext = "DATASET ACTIVATE main.\n"

compute_p = """COMPUTE mrpoint=mrim1p + mrim2p + mrim3p +mrii1p + mrii2p + mrii3p+ mrbm1p + mrbm2p + mrbm3p+mrbi1p + mrbi2p + mrbi3p.
"""
compute_g = """COMPUTE mrgist=mrim1g + mrim2g + mrim3g +mrii1g + mrii2g + mrii3g+ mrbm1g + mrbm2g + mrbm3g+mrbi1g + mrbi2g + mrbi3g.
"""
compute_sent = """COMPUTE mrsent=mrimsent + mriisent + mrbmsent + mrbisent.
"""
compute_para = """COMPUTE mrpara = mrimpara + mriipara + mrbmpara + mrbipara.
"""


text1 = """DATASET COPY  mainCopy1 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy1.\n"""

## POINTS ##


f.write(text1)
f.write(compute_p)
f.write("FREQUENCIES variables = mrpoint \n/STATISTICS = mean sum\n/ORDER=ANALYSIS.\n")
f.write(switchtext)
f.write("DATASET CLOSE mainCopy1.\n")

text2 = """DATASET COPY  mainCopy2 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy2.\n"""

## GISTS ##

f.write(text2)
f.write(compute_g)
f.write("FREQUENCIES variables = mrgist \n/STATISTICS = mean sum\n/ORDER=ANALYSIS.\n")
f.write(switchtext)
f.write("DATASET CLOSE mainCopy2.\n")
  
text3 = """DATASET COPY  mainCopy3 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy3.\n"""

## SENTENCES ##

f.write(text3)
f.write(compute_sent)
f.write("FREQUENCIES variables = mrsent \n/STATISTICS = mean sum\n/ORDER=ANALYSIS.\n")
f.write(switchtext)
f.write("DATASET CLOSE mainCopy3.\n")

text4 = """DATASET COPY  mainCopy4 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy4.

recode mrimpara mriipara mrbmpara mrbipara (1=1) (2=2) (3=3) (else = 0).\n"""

## PARAGRAPHS ##

f.write(text4)
f.write(compute_para)
f.write("FREQUENCIES variables = mrpara \n/STATISTICS = mean sum\n/ORDER=ANALYSIS.\n")
f.write(switchtext)
f.write("DATASET CLOSE mainCopy4.\n")