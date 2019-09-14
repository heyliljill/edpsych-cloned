def main():  
 
  f = open('romathstratspintdiff.txt','w+')
  
  # VARIABLES
  nameList = ['par', 'sen', 'key', 'kc', 'kn', 'num', 'eli', 'use', 'est', 'rea', 'rec', 'ren', 'para', 'vis', 'ske', 'per', 'pri', 're1', 'gue']
  labelList= ['parts', 'sentence', 'keywords', 'keywordscontext', 'keywordsnumbers', 'numbers', 'eliminatekeys', 'usesallnum', 'estimate', 'reasonable', 'rereadscomp', 'rereadsnum', 'paraphrase', 'visualze', 'sketch', 'personalexp', 'priorknow', 'readthrough1st', 'guess']
  proquestions = ['1','2','3','4','5','6','7','8','9','a','b','c']

  suffix = ['im','ii','nm','ni']
 
  stratdiff = "s"
  promain= "p"
  mathread = "m"
  templine = "Temporary.\n"


  for j in range(1,4):
    ## SELECT HIGH INTEREST ## 
    
    if mathread == "m":
      spint = "mathspint"
    elif mathread == "r":
      spint = "readspint"
    
    filterText = """USE ALL. \nCOMPUTE filter_$=("""+spint+"="+ str(j) +"""). \nVARIABLE LABELS filter_$ '""" + spint+"="+ str(j) +"""(FILTER)'. \nVALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. \nFORMATS filter_$ (f1.0). \nFILTER BY filter_$. \nEXECUTE.\n\n"""
  
    f.write(filterText)
    
    for i in range(len(nameList)):
      #RECODE AND COMPUTE AND SELECT
      nameListi = nameList[i]
      labelListi = labelList[i]    
      recodeline = makeRecodeLine(proquestions,promain,mathread,stratdiff,nameListi)
      computelines = makeComputeLines(proquestions,promain,mathread,stratdiff,nameListi,labelListi)
      selectifline = makeSelectLine(proquestions,promain,mathread,stratdiff,nameListi)
      
      frequenciesline ="FREQUENCIES variables = "+labelListi+"mastery "+labelListi+"instructional"+"\n"
      
      statisticsorder = "/STATISTICS = mean sum\n/ORDER=ANALYSIS.\n\n\n\n"
      
      s = templine + recodeline+computelines+frequenciesline+statisticsorder
      
      f.write(s)
    
    ## REMOVE FILTER ##
    
    f.write("""FILTER OFF.\nUSE ALL.\nEXECUTE.\n\n""")
def makeRecodeLine(proquestions,promain,mathread,stratdiff,nameListi):
  recodevars = ""
  if mathread == "m":
    for i in range(len(proquestions)):
      recodevars = recodevars+promain+mathread+proquestions[i]+stratdiff+nameListi+" "
  else:
    for i in range(len(proquestions)):
      recodevars = recodevars+promain+mathread+proquestions[i]+nameListi+" "
  recodeline = "recode "+recodevars+"(1=1) (2=1) (else = 0).\n"
  return recodeline
  
  
def makeComputeLines(proquestions,promain,mathread,stratdiff,nameListi,labelListi):
  computeIMVars = makeComputeLine('im',0,3,proquestions,promain,mathread,stratdiff,nameListi)
  computeIIVars = makeComputeLine('ii',3,6,proquestions,promain,mathread,stratdiff,nameListi)
  computeNMVars = makeComputeLine('nm',6,9,proquestions,promain,mathread,stratdiff,nameListi)
  computeNIVars = makeComputeLine('ni',9,12,proquestions,promain,mathread,stratdiff,nameListi)

  # computeIMLine = "compute "+labelListi+"im"+"="+computeIMVars+".\n"
  # computeIILine = "compute "+labelListi+"ii"+"="+computeIIVars+".\n"
  # computeNMLine = "compute "+labelListi+"nm"+"="+computeNMVars+".\n"
  # computeNILine = "compute "+labelListi+"ni"+"="+computeNIVars+".\n"
  
  computeMasteryLine = "compute "+labelListi+"mastery"+"="+computeIMVars+"+"+computeNMVars+".\n"
  computeInstructionalLine = "compute "+labelListi+"instructional"+"="+computeIIVars+"+"+computeNIVars+".\n"
  
  return computeMasteryLine + computeInstructionalLine
  
def makeComputeLine(suffix,rangeL,rangeU,proquestions,promain,mathread,stratdiff,nameListi):
  computeVars = ""
  if mathread =="m":
    for i in range(rangeL,rangeU):
      computeVars = computeVars+promain+mathread+proquestions[i]+stratdiff+nameListi+" "
      if (i!=rangeU-1):
        computeVars = computeVars+ "+ "
  else:
    for i in range(rangeL,rangeU):
      computeVars = computeVars+promain+mathread+proquestions[i]+nameListi+" "
      if (i!=rangeU-1):
        computeVars = computeVars+ "+ "
  return computeVars
  
def makeSelectLine(proquestions,promain,mathread,stratdiff,nameListi):
  selectifvars = ""
  if mathread == "m":
    for i in range(len(proquestions)):
      selectifvars = selectifvars+promain+mathread+proquestions[i]+stratdiff+nameListi+" "
      if (i!=len(proquestions)-1):
        selectifvars = selectifvars+ "or "
  else:
    for i in range(len(proquestions)):
      selectifvars = selectifvars+promain+mathread+proquestions[i]+nameListi+" "
      if (i!=len(proquestions)-1):
        selectifvars = selectifvars+ "or "
  selectifline = "SELECT IF ("+selectifvars+" = 1 ).\n\n"
  return selectifline
 

main()
