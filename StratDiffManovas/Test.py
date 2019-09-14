import GLMfunctions

def main():
  # TEST
  f = open('test.txt','w+')
  
  # VARIABLES
  nameList = ['vo', 'gc','ac','sk', 'pp', 'kt', 'kc','de', 'cv','fp','fa','ya','na', 'nv','nc','in','nt','tg','di','nd']
  labelList= ['vocab','generalcomp','factuncertainty','seperating','confuseprevious','lacktopicknow','lackcontentknow','toodetailed','cantverbalize','forgetparagraph','forgetall','positiveaffect','negativeaffect','nervous','noconcentrate','interviewerprocedure','notalki', 'toogeneral','distractor','nodifficulties']
  proquestions = ['1','2','3']
  suffix = ['im','ii','bm','bi']
  
  stratdiff = "d"
  promain= "p"
  mathread = "r"
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
  
  readdiff1 = ["vocab", "generalcomp", "lackcontentknow"]
  readdiff2 = ["toodetailed", "forgetall"]
  readdiff3 = ["negativeaffect", "toogeneral"]
  
  GLMfunctions.printCompute(readdiff1,"readdiff1",suffix,GLMtext,f)
  GLMfunctions.printCompute(readdiff2,"readdiff2",suffix,GLMtext,f)
  GLMfunctions.printCompute(readdiff3,"readdiff3",suffix,GLMtext,f)
  
  # Recall vs encoding vs comprehension monitoring   
  recall = ['cantverbalize','forgetparagraph','forgetall','nervous','noconcentrate','notalki', 'toogeneral','distractor'] 
  encoding = ['vocab','generalcomp','factuncertainty','seperating','confuseprevious','lacktopicknow','lackcontentknow','toodetailed','positiveaffect','negativeaffect'] 
  compmonitor = [] 
   
  # Rehearsal vs elaboration vs organizational vs comprehension monitoring vs affective/motivational 
  rehearsal = ['cantverbalize','forgetparagraph','forgetall'] 
  elaboration = ['lacktopicknow','lackcontentknow','positiveaffect','negativeaffect'] 
  organizational = ['vocab','generalcomp','factuncertainty','seperating','confuseprevious','toodetailed','toogeneral'] 
  compmonitor2 = ['notalki'] 
  affectivemot = ['nervous','noconcentrate','distractor'] 
   
  #Basic vs complex for rehearsal, elaboration, organizational 
  rehearsalb = ['cantverbalize','forgetparagraph','forgetall'] 
  elaborationb = [] 
  organizationalb = ['vocab','generalcomp','confuseprevious','toodetailed','toogeneral'] 
  rehearsalc = [] 
  elaborationc = ['lacktopicknow','lackcontentknow','positiveaffect','negativeaffect'] 
  organizationalc = ['factuncertainty','seperating'] 
   
  selection = ['confuseprevious','toodetailed','positiveaffect','negativeaffect'] 
  acquisition = ['vocab','generalcomp'] 
  construction = ['factuncertainty'] 
  integration = ['seperating','lacktopicknow','lackcontentknow'] 
   
   
   
  allgroups = [recall,encoding,compmonitor,rehearsal, elaboration, organizational, compmonitor2, affectivemot, rehearsalb, elaborationb, organizationalb, rehearsalc, elaborationc, organizationalc, selection, acquisition, construction, integration] 
  allgroupsname = ['recall','encoding','compmonitor','rehearsal', 'elaboration', 'organizational', 'compmonitor2', 'affectivemot', 'rehearsalb', 'elaborationb', 'organizationalb', 'rehearsalc', 'elaborationc', 'organizationalc', 'selection', 'acquisition', 'construction', 'integration'] 
   
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
 


main()