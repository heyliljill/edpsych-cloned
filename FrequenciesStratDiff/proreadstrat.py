f = open('proreaddstrat.txt','w+')

#This produces code for calculating strategy frequencies

nameList = ['ptp', 'gtp','ttb','btt', 'th1', 'fin', 'nov','dnn', 'ver','tid','pex','pkn','eye', 'agn','ide','ktw']
labelList= ['point2point', 'gist2point', 'top2bottom', 'bottom2top', 'firstthing', 'lastthing', 'novelinfo', 'datesnumnames', 'concurrentverb', 'duringdistractor', 'personalexp', 'generalknowledge', 'visualizations', 'repitition','mainidea', 'keytopicword']
proquestions = ['1s1','1s2','1s3', '2s1', '2s2', '2s3', '3s1', '3s2', '3s3', '4s1','4s2','4s3']

for j in range(0,4):
  for i in range(len(nameList)):
    nameListi = nameList[i]
    labelListi = labelList[i]
    value = str(j)
    promain= "p"
    mathread = "r"

    templine = "Temporary.\n"

    recodevars = ""
    for i in range(len(proquestions)):
      recodevars = recodevars+promain+mathread+proquestions[i]+nameListi+" "

    recodeline = "recode "+recodevars+"("+value+"=1) (else = 0).\n"

    selectifvars = ""
    for i in range(len(proquestions)):
      selectifvars = selectifvars+promain+mathread+proquestions[i]+nameListi+" "
      if (i!=len(proquestions)-1):
        selectifvars = selectifvars+ "or "

    selectifline = "SELECT IF ("+selectifvars+" = 1 ).\n\n"

    computevars = ""

    for i in range(len(proquestions)):
      computevars = computevars+promain+mathread+proquestions[i]+nameListi+" "
      if (i!=len(proquestions)-1):
        computevars = computevars+ "+ "

    computeline = "compute "+labelListi+"="+computevars+".\n\n"

    frequenciesline ="FREQUENCIES variables = "+labelListi+"\n"

    statisticsorder = "/STATISTICS = mean sum\n/ORDER=ANALYSIS.\n\n\n\n"
          
    s = templine+recodeline+selectifline+computeline+frequenciesline+statisticsorder
          
    f.write(s)
