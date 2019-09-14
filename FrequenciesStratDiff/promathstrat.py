f = open('promathstrat.txt','w+')

nameList = ['par', 'sen', 'key', 'kc', 'kn', 'num', 'eli', 'use', 'est', 'rea', 'rec', 'ren', 'para', 'vis', 'ske', 'per', 'pri', 're1', 'gue']
labelList= ['parts', 'sentence', 'keywords', 'keywordscontext', 'keywordsnumbers', 'numbers', 'eliminatekeys', 'usesallnum', 'estimate', 'reasonable', 'rereadscomp', 'rereadsnum', 'paraphrase', 'visualze', 'sketch', 'personalexp', 'priorknow', 'readthrough1st', 'guess']
proquestions = ['1','2','3','4','5','6','7','8','9','a','b','c']

for j in range(0,4):
  for i in range(len(nameList)):
    nameListi = nameList[i]
    labelListi = labelList[i]
    value = str(j)
    stratdiff = "s"
    promain= "p"
    mathread = "m"

    templine = "Temporary.\n"

    recodevars = ""
    for i in range(len(proquestions)):
      recodevars = recodevars+promain+mathread+proquestions[i]+stratdiff+nameListi+" "

    recodeline = "recode "+recodevars+"("+value+"=1) (else = 0).\n"

    selectifvars = ""
    for i in range(len(proquestions)):
      selectifvars = selectifvars+promain+mathread+proquestions[i]+stratdiff+nameListi+" "
      if (i!=len(proquestions)-1):
        selectifvars = selectifvars+ "or "

    selectifline = "SELECT IF ("+selectifvars+" = 1 ).\n\n"

    computevars = ""

    for i in range(len(proquestions)):
      computevars = computevars+promain+mathread+proquestions[i]+stratdiff+nameListi+" "
      if (i!=len(proquestions)-1):
        computevars = computevars+ "+ "

    computeline = "compute "+labelListi+"="+computevars+".\n\n"

    frequenciesline ="FREQUENCIES variables = "+labelListi+"\n"

    statisticsorder = "/STATISTICS = mean sum\n/ORDER=ANALYSIS.\n\n\n\n"
         
    s = templine+recodeline+selectifline+computeline+frequenciesline+statisticsorder
         
    f.write(s)

