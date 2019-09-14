# 5.(Table 7) mean number of corrections, by type, out of 12 problems
# a. another step (pmim1ano), computational (pmim1com), copying (pmim1cop), operation/key (pmim1opk), operations choice (pmim1opc)
# b. Break up into interest, difficulty, gender

# pmano = pmim1ano + pmim2ano + pmim3ano...

# pmcom = pmim1com + pmim2com + pmim3com...

# pmcop = pmim1cop + pmim2cop + pmim3cop... 

# pmopk = pmim1opk + pmim2opk + pmim3opk ...

# pmopc = pmim1opc + pmim2opc + pmim3opc... 


f = open('PMcorrections.txt','w+')

#This produces code for calculating frequencies for math variables


levels = ["im","ii","bm","bi"]
prefix = "pm"
suffix = ["ano","com","cop","opk","opc"]
types = [1]
 

switchtext = "DATASET ACTIVATE pro.\n"
# repeat for each type
for i in range(len(suffix)):
    computeline = "COMPUTE "+prefix+suffix[i]+" = "
    recodeline = "recode "
    variablelabels = """VARIABLE LABELS  """+prefix+suffix[i]+""" \'# of corrections from all problems\'.\nEXECUTE.\n"""

    for lv in levels:
    #gets im, ii, bm, bi
        for k in range(1,4):
            #gets im1, im2, im3..
            variable = prefix + lv + str(k) + suffix[i]
            computeline = computeline + variable + " + "
            recodeline = recodeline + variable + " "
    computeline = computeline.rstrip('+ ')+ ".\n"   
    
    
    frequencies = "FREQUENCIES variables = "+prefix+suffix[i]+"\n/STATISTICS = mean sum\n/ORDER=ANALYSIS.\n"
    
    f.write("DATASET NAME pro.\n")
    
    copytext = """DATASET COPY  proCopy"""+str(i)+""" WINDOW=FRONT.\nDATASET ACTIVATE proCopy"""+str(i)+""".\n"""
    
    f.write(copytext)
    f.write(computeline)
    f.write(variablelabels)
    f.write(frequencies)
    f.write(switchtext)
    f.write("DATASET CLOSE proCopy"+str(i)+".\n\n")