f = open('proreaddiff.txt','w+')

#This produces code for calculating strategy frequencies

nameList = ['voc', 'gen','acc','sep', 'prp', 'nkt', 'nkc','det', 'tor','par','all','yea','bum', 'ner','huh','int','ncv','tge','dis','nod']
labelList= ['vocab','generalcomp','factuncertainty','seperating','confuseprevious','lacktopicknow','lackcontentknow','toodetailed','cantverbalize','forgetparagraph','forgetall','positiveaffect','negativeaffect','nervous','noconcentrate','interviewerprocedure','notalki', 'toogeneral','distractor','nodifficulties']
proquestions = ['1d1','1d2','1d3', '2d1', '2d2', '2d3', '3d1', '3d2', '3d3', '4d1','4d2','4d3']

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
      selectifvars = selectifvars+promain+mathread+proquestions[1]+nameListi+" "
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

    print s
