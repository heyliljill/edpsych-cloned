# 	a. (mmim1lb1, mmim2lb1, mmmim3lb1... 12 total). Unit in label. none = 0, correct = 1, incorrect = 2, variation = 3, interpretation = 4 
#   b. (mmim1lb2, mmim2lb2, mmmim3lb2... 12 total). Context of label. none = 0, minimal = 1, full = 2, incorrect = 3, general = 4
#   c. (mmim1lb3, mmim2lb3, mmmim3lb3... 12 total). Sentence for label. no = 0, yes = 1. 


f = open('MMlabels.txt','w+')

#This produces code for calculating frequencies for math variables
# There are 3 suffixes. lb1 (unit) lbl2 (context) lbl3 (sentence)

f.write("""USE ALL.
COMPUTE filter_$=(pro = 0).
VARIABLE LABELS filter_$ 'pro = 0 (FILTER)'.
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'.
FORMATS filter_$ (f1.0).
FILTER BY filter_$.
EXECUTE.""")




levels = ["im","ii","bm","bi"]
prefix = "mm"
suffix = "lb1"
types =  [0,1,2,3,4]

computeline = "COMPUTE labels = "
recodeline = "recode "
variablelabels = """VARIABLE LABELS  """+prefix+suffix+""" \'# of unit label types from all problems\'.EXECUTE.\n"""

switchtext = "DATASET ACTIVATE main.\n"
# repeat for each type
for i in range(len(types)):
    computeline = "COMPUTE "+prefix+suffix+" = "
    recodeline = "recode "
    variablelabels = """VARIABLE LABELS  """+prefix+suffix+""" \'# of mistake types from all problems\'.\nEXECUTE.\n"""

    for lv in levels:
    #gets im, ii, bm, bi
        for k in range(1,4):
            #gets im1, im2, im3..
            variable = prefix + lv + str(k) + suffix
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
    
### Repeat for 2nd label ###
levels = ["im","ii","bm","bi"]
prefix = "mm"
suffix = "lb2"
types = [0,1,2,3,4]

for i in range(len(types)):
    computeline = "COMPUTE "+prefix+suffix+" = "
    recodeline = "recode "
    variablelabels = """VARIABLE LABELS  """+prefix+suffix+""" \'# of mistake types from all problems\'.\nEXECUTE.\n"""

    for lv in levels:
    #gets im, ii, bm, bi
        for k in range(1,4):
            #gets im1, im2, im3..
            variable = prefix + lv + str(k) + suffix
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


### Repeat for 3rd label ###
levels = ["im","ii","bm","bi"]
prefix = "mm"
suffix = "lb3"
types = [1]

for i in range(len(types)):
    computeline = "COMPUTE "+prefix+suffix+" = "
    recodeline = "recode "
    variablelabels = """VARIABLE LABELS  """+prefix+suffix+""" \'# of mistake types from all problems\'.\nEXECUTE.\n"""

    for lv in levels:
    #gets im, ii, bm, bi
        for k in range(1,4):
            #gets im1, im2, im3..
            variable = prefix + lv + str(k) + suffix
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