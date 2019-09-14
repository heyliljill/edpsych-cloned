import GLMfunctions

def main():
  
  #(MANOVA?) GLM general linear model with within subject comparisons of interest, gender, diff
  f = open('manova-proreadstratspint.txt','w+')

  # VARIABLES
  nameList = ['pp', 'gp','tb','bt', 't1', 'tl', 'ni','dn', 'cv','td','pe','kn','uv', 'rp','ya','na']
  labelList= ['point2point', 'gist2point', 'top2bottom', 'bottom2top', 'firstthing', 'lastthing', 'novelinfo', 'datesnumnames', 'concurrentverb', 'duringdistractor', 'personalexp', 'generalknowledge', 'visualizations', 'repitition','mainidea', 'keytopicword']
  proquestions = ['1','2','3']
  suffix = ['im','ii','bm','bi']
 
  stratdiff = "s"
  promain= "p"
  mathread = "r"
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
      computelines = GLMfunctions.(suffix,proquestions,promain,mathread,stratdiff,nameListi,labelListi)
    
      s = recodeline+computelines
      
      f.write(s)
    
      # GLM
      text = "GLM " + labelListi+"im "+ labelListi+"ii "+ labelListi+"bm "+ labelListi+"bi "+"BY sex"
      f.write(text)
      f.write(GLMtext)
      f.write('\n')
    
    # GROUPED
    
    readstrat1 = ["point2point", "top2bottom"]
  
    GLMfunctions.(readstrat1,"readstrat1",suffix,GLMtext,f)
  
    recall = ['point2point', 'gist2point', 'top2bottom', 'bottom2top', 'firstthing', 'lastthing'] 
    encoding = ['novelinfo', 'datesnumnames','personalexp','generalknowledge','visualizations','mainidea','keytopicword'] 
    compmonitor = ['concurrentverb','duringdistractor','repitition'] 
     
    # Rehearsal vs elaboration vs organizational vs comprehension monitoring vs affective/motivational 
    rehearsal = ['duringdistractor', 'repitition'] 
    elaboration = ['novelinfo','datesnumnames','personalexp','generalknowledge','visualizations'] 
    organizational = ['point2point', 'gist2point', 'top2bottom', 'bottom2top', 'firstthing', 'lastthing','mainidea','keytopicword'] 
    compmonitor2 = ['concurrentverb'] 
    affectivemot = [] 
     
    #Basic vs complex for rehearsal, elaboration, organizational 
    rehearsalb = ['repitition'] 
    elaborationb = ['novelinfo','datesnumnames','personalexp','generalknowledge','visualizations'] 
    organizationalb = ['point2point', 'top2bottom', 'bottom2top', 'firstthing', 'lastthing'] 
    rehearsalc = ['duringdistractor'] 
    elaborationc = [] 
    organizationalc = ['gist2point','mainidea','keytopicword'] 
     
    selection = ['novelinfo','datesnumnames'] 
    acquisition = [] 
    construction = ['visualizations','mainidea','keytopicword'] 
    integration = ['personalexp','generalknowledge'] 
        
     
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
    ## REMOVE FILTER ##
    
    f.write("""FILTER OFF.\nUSE ALL.\nEXECUTE.\n\n""")
    
################################################################################    

main()
  