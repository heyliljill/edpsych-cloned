f = open('PRaccuracy.txt','w+')

#This produces code for calculating frequencies for reading variables


f.write("""USE ALL.
COMPUTE filter_$=(pro = 1).
VARIABLE LABELS filter_$ 'pro = 1 (FILTER)'.
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'.
FORMATS filter_$ (f1.0).
FILTER BY filter_$.
EXECUTE.

""")


levels = ["im","ii","bm","bi"]
prefix = "mr"
suffix = "acc"
types = [1,2,3,4]


switchtext = "DATASET ACTIVATE main.\n"
# repeat for each type
for i in range(len(types)):
    computeline = "COMPUTE "+prefix+suffix+" = "
    recodeline = "recode "
    variablelabels = """VARIABLE LABELS  """+prefix+suffix+""" \'# of accuracy level types from all problems\'.\nEXECUTE.\n"""

    for lv in levels:
    #gets im, ii, bm, bi
        variable = prefix + lv + suffix
        computeline = computeline + variable + " + "
        recodeline = recodeline + variable + " "
    computeline = computeline.rstrip('+ ')+ ".\n"   
    
    recodeline = recodeline + "("+str(types[i])+"=1) (else = 0).\n"
    
    frequencies = "FREQUENCIES variables = "+prefix+suffix+"\n/STATISTICS = mean sum\n/ORDER=ANALYSIS.\n"
    
    f.write("DATASET NAME main.\n")
    
    copytext = """DATASET COPY  mainCopy"""+str(types[i])+""" WINDOW=FRONT.\nDATASET ACTIVATE mainCopy"""+str(types[i])+""".\n"""
    
    f.write(copytext)
    f.write(recodeline)
    f.write(computeline)
    f.write(variablelabels)
    f.write(frequencies)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy"+str(types[i])+".\n\n")
    
f.write("""FILTER OFF. 
USE ALL. 
EXECUTE.""")