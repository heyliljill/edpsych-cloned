## computational (=4), copying (=5), partial set-up (=2), set-up (=1), unattempted (=6), unfinished (=3)

f = open('MMmistakesSPINT.txt','w+')

#This produces code for calculating frequencies for math variables
#COMPUTE mmrw = mmim1rw + mmim2rw + mmim3rw + mmii1rw... 


f.write("""USE ALL.
COMPUTE filter_$=(pro = 0).
VARIABLE LABELS filter_$ 'pro = 0 (FILTER)'.
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'.
FORMATS filter_$ (f1.0).
FILTER BY filter_$.
EXECUTE.""")


mathread = "m"

for i in range(0,2):
    ## SELECT HIGH INTEREST ## 
    filtersign = ["~=","="]
    if mathread == "m":
      spint = "mathspint"
    elif mathread == "r":
      spint = "readspint"
    
    filterText = """USE ALL. \nCOMPUTE filter_$=("""+spint+filtersign[i]+ "2"+"""). \nVARIABLE LABELS filter_$ '""" + spint+filtersign[i]+ "2" +"""(FILTER)'. \nVALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. \nFORMATS filter_$ (f1.0). \nFILTER BY filter_$. \nEXECUTE.\n\n"""
    
    f.write(filterText)

    levels = ["im","ii","bm","bi"]
    prefix = "mm"
    suffix = "mis"
    types = [1,2,3,4,5,6]
    
    
     
    
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
        
f.write("""FILTER OFF.
USE ALL.
EXECUTE.""")