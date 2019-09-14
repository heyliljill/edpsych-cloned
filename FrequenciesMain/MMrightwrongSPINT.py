f = open('MMrightwrongSPINT.txt','w+')

#This produces code for calculating frequencies for math variables
#COMPUTE mmrw = mmim1rw + mmim2rw + mmim3rw + mmii1rw... 
# THIS ONE IS WONKY BECAUSE ITS JUST 1 VARIABLE

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
    suffix = "rw"
    
    computeline = "COMPUTE "+prefix+suffix+" = "
    recodeline = "recode "
    variablelabels = """VARIABLE LABELS  mmrw \'# of correct answers from all problems\'.\nEXECUTE.\n"""
    
    for lv in levels:
        #gets im, ii, bm, bi
        for k in range(1,4):
            #gets im1, im2, im3..
            variable = prefix + lv + str(k) + suffix
            computeline = computeline + variable + " + "
            recodeline = recodeline + variable + " "
    computeline = computeline.rstrip('+ ')+ ".\n"   
    recodeline = recodeline + "(1=1) (else = 0).\n"
        
    frequencies = "FREQUENCIES variables = "+prefix+suffix+"\n/STATISTICS = mean sum\n/ORDER=ANALYSIS.\n"
    
    switchtext = "DATASET ACTIVATE main.\n"
    
    f.write("DATASET NAME main.\n")
    
    text1 = """DATASET COPY  mainCopy1 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy1.\n"""
    
    f.write(text1)
    #f.write(recodeline)
    f.write(computeline)
    f.write(variablelabels)
    f.write(frequencies)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy1.\n\n")

f.write("""FILTER OFF.
USE ALL.
EXECUTE.""")
