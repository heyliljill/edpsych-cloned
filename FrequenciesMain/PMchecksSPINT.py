## no check (=1), can't tell (=2), computation (=3), operation (=4), reasonableness (=5), alternate set-up (=6)

f = open('PMchecksSPINT.txt','w+')

#This produces code for calculating frequencies for math variables
#COMPUTE pmchk = pmim1chk + pmim2chk + pmim3chk + pmim4chk... 


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
    prefix = "pm"
    suffix = "chk"
    types = [1,2,3,4,5,6]
    
    
     
    
    switchtext = "DATASET ACTIVATE pro.\n"
    # repeat for each type
    for i in range(len(types)):
        computeline = "COMPUTE "+prefix+suffix+" = "
        recodeline = "recode "
        variablelabels = """VARIABLE LABELS  """+prefix+suffix+""" \'# of check types from all problems\'.\nEXECUTE.\n"""
    
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
        
        f.write("DATASET NAME pro.\n")
        
        copytext = """DATASET COPY  proCopy"""+str(types[i])+""" WINDOW=FRONT.\nDATASET ACTIVATE proCopy"""+str(types[i])+""".\n"""
        
        f.write(copytext)
        f.write(recodeline)
        f.write(computeline)
        f.write(variablelabels)
        f.write(frequencies)
        f.write(switchtext)
        f.write("DATASET CLOSE proCopy"+str(types[i])+".\n\n")
        
        
f.write("""FILTER OFF.
USE ALL.
EXECUTE.""")