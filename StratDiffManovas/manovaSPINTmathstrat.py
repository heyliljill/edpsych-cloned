import GLMfunctions

def main():

  # (MANOVA?) GLM general linear model with within subject comparisons of interest, gender, diff
  
  f = open('manova-promathstratspint.txt','w+')
  
  # VARIABLES
  nameList = ['pa', 'ss', 'ky', 'kc', 'kn', 'nm', 'el', 'un', 'es', 're', 'rc', 'rn', 'sp', 'vi', 'sk', 'pe', 'pk', 'r1', 'gu'] 
  labelList= ['parts', 'sentence', 'keywords', 'keywordscontext', 'keywordsnumbers', 'numbers', 'eliminatekeys', 'usesallnum', 'estimate', 'reasonable', 'rereadscomp', 'rereadsnum', 'paraphrase', 'visualize', 'sketch', 'personalexp', 'priorknow', 'readthrough1st', 'guess']
  proquestions = ['1','2','3']
  suffix = ['im','ii','bm','bi']
 
  stratdiff = "s"
  promain= "p"
  mathread = "m"
  GLMtext = GLMfunctions.makeGLMtext()
 
  f.write("DATASET COPY  proCopy WINDOW=FRONT.\nDATASET ACTIVATE proCopy.\n")

  for i in range(1,3):
    ## SELECT HIGH INTEREST ## 
    
    if mathread == "m":
      spint = "mathspint"
    elif mathread == "r":
      spint = "readspint"
    
    filterText = """USE ALL. \nCOMPUTE filter_$=("""+spint+"="+ str(i) +"""). \nVARIABLE LABELS filter_$ '""" + spint+"="+ str(i) +"""(FILTER)'. \nVALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. \nFORMATS filter_$ (f1.0). \nFILTER BY filter_$. \nEXECUTE.\n\n"""
  
    f.write(filterText)
    
    for i in range(len(nameList)):
      #RECODE AND COMPUTE
      nameListi = nameList[i]
      labelListi = labelList[i]    
      recodeline = GLMfunctions.makeRecodeLine(suffix,proquestions,promain,mathread,stratdiff,nameListi)
      computelines = GLMfunctions.makeComputeLines(suffix,proquestions,promain,mathread,stratdiff,nameListi,labelListi)
    
      s = recodeline+computelines
      
      f.write(s)
    
      # GLM
      text = "GLM " + labelListi+"im "+ labelListi+"ii "+ labelListi+"bm "+ labelListi+"bi "+"BY sex"
      f.write(text)
      f.write(GLMtext)
      f.write('\n')
    
    
    # GROUPED
    
    mathstrat1 = ["sentence", "usesallnum"]
    mathstrat3 = ["paraphrase", "visualize"]
    mathstrat5 = ["eliminatekeys", "rereadsnum"]
    
    GLMfunctions.printCompute(mathstrat1,"mathstrat1",suffix,GLMtext,f)
    GLMfunctions.printCompute(mathstrat3,"mathstrat3",suffix,GLMtext,f)
    printCompute(mathstrat5,"mathstrat5",suffix,GLMtext,f)
    
    # Rehearsal vs elaboration vs organizational vs comprehension monitoring vs affective/motivational 
    rehearsal = [] 
    elaboration = ['paraphrase','visualize','sketch','personalexp','priorknow'] 
    organizational = ['parts', 'sentence', 'keywords', 'keywordscontext', 'keywordsnumbers', 'numbers', 'eliminatekeys', 'usesallnum'] 
    compmonitor2 = ['estimate','reasonable','rereadscomp','rereadsnum','readthrough1st'] 
    affectivemot = [] 
     
    #Basic vs complex for rehearsal, elaboration, organizational 
    rehearsalb = [] 
    elaborationb = ['visualize','sketch'] 
    organizationalb = ['numbers','eliminatekeys','usesallnum'] 
    rehearsalc = [] 
    elaborationc = ['paraphrase','personalexp','priorknow'] 
    organizationalc = ['parts','sentence','keywords','keywordscontext','keywordsnumbers'] 
     
     
    allgroups = [rehearsal, elaboration, organizational, compmonitor2, affectivemot, rehearsalb, elaborationb, organizationalb, rehearsalc, elaborationc, organizationalc] 
    allgroupsname = ['rehearsal', 'elaboration', 'organizational', 'compmonitor2', 'affectivemot', 'rehearsalb', 'elaborationb', 'organizationalb', 'rehearsalc', 'elaborationc', 'organizationalc'] 
     
  
    for k in range(len(allgroups)):
      for j in range(len(suffix)):
        f.write("compute " + allgroupsname[k] + suffix[j] +" = (")
        for i in range(len(allgroups[k])):
          if i != 0:
            f.write("+")
          f.write(allgroups[k][i]+suffix[j])
        f.write(")/" + str(len(allgroups[k])) + ".\n")
    
      f.write("\n\nGLM") 
    
      for j in range(len(suffix)):
        f.write(" "+ allgroupsname[k]+suffix[j])
      f.write(" BY sex") 
      f.write(GLMtext + "\n")
  
    ## REMOVE FILTER ##
    
    f.write("""FILTER OFF.\nUSE ALL.\nEXECUTE.\n\n""")
  


main()
  
  

