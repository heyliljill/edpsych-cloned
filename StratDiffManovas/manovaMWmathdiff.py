import GLMfunctions

def main():
  
  # (MANOVA?) GLM general linear model with within subject comparisons of interest, gender, diff

  f = open('manova-promathdiff.txt','w+')
  
  # VARIABLES
  nameList = ['su', 'sp', 'cd', 'cp', 'ck', 'cv', 'ex', 'td', 'lk','ua', 'qu', 'pa', 'na', 'ct']
  labelList= ['setup', 'partialsetup', 'comprehension', 'comprehensionparts', 'keywordcomprehension', 'vocabcomprehension', 'extramissinginfo', 'toodetailed', 'lackknowledge', 'unreasonable', 'questiondifficulty', 'positiveaffect', 'negativeaffect', 'concentration']
  proquestions = ['1','2','3']
  suffix = ['im','ii','bm','bi']

 
  stratdiff = "d"
  promain= "p"
  mathread = "m"
  GLMtext = GLMfunctions.makeGLMtext()
  
  f.write("DATASET COPY  proCopy WINDOW=FRONT.\nDATASET ACTIVATE proCopy.\n")
 
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

  mathdiff1 = ["setup", "comprehension", "extramissinginfo", "toodetailed", "partialsetup", "negativeaffect", "questiondifficulty"]
  mathdiff2 = ["vocabcomprehension", "lackknowledge", "comprehensionparts"]
 
  GLMfunctions.printCompute(mathdiff1,"mathdiff1",suffix,GLMtext,f)
  GLMfunctions.printCompute(mathdiff2,"mathdiff2",suffix,GLMtext,f)


  # Rehearsal vs elaboration vs organizational vs comprehension monitoring vs affective/motivational
  rehearsal = ['keywordcomprehension','vocabcomprehension','questiondifficulty']
  elaboration = ['comprehension','comprehensionparts','lackknowledge','positiveaffect','negativeaffect']
  organizational = ['setup','partialsetup','toodetailed']
  compmonitor2 = ['extramissinginfo','unreasonable']
  affectivemot = ['concentration']
  
  #Basic vs complex for rehearsal, elaboration, organizational
  rehearsalb = ['keywordcomprehension','vocabcomprehension','questiondifficulty']
  elaborationb = ['lackknowledge']
  organizationalb = ['setup','partialsetup','toodetailed']
  affectivemotb = []
  rehearsalc = []
  elaborationc = ['comprehension','comprehensionparts','positiveaffect','negativeaffect']
  organizationalc = []
  
  
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

############################################################################

main()