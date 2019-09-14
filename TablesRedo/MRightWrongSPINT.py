# Math Right Wrong. mean number of correct answers, out of 12 problems (mmim1rw, mmim2rw, mmmim3rw... 12 total)



# mmimrw = mmim1rw + mmim2rw + mmim3rw 
# mmiirw = mmii1rw + mmii2rw + mmii3rw
# mmbmrw = mmbm1rw + mmbm2rw + mmbm3rw
# mmbirw = mmbi1rw + mmbi2rw + mmbi3rw 


f = open('manova-rightwrongSPINT','w+')

def main():
  
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
    
    GLMtext = """
  GLM mmimrw mmiirw mmbmrw mmbirw BY sex
    /WSFACTOR=interest 2 Polynomial diff 2 Polynomial 
    /METHOD=SSTYPE(3) 
    /EMMEANS=TABLES(sex) COMPARE ADJ(LSD) 
    /EMMEANS=TABLES(interest) COMPARE ADJ(LSD) 
    /EMMEANS=TABLES(diff) COMPARE ADJ(LSD) 
    /EMMEANS=TABLES(sex*interest) 
    /EMMEANS=TABLES(sex*diff) 
    /EMMEANS=TABLES(interest*diff) 
    /EMMEANS=TABLES(sex*interest*diff) 
    /CRITERIA=ALPHA(.05) 
    /WSDESIGN=interest diff interest*diff 
    /DESIGN=sex.
  
    """
    
    compute = """COMPUTE mmimrw = mmim1rw + mmim2rw + mmim3rw. 
  VARIABLE LABELS  mmimrw '# of correct answers from all problems in interest mastery level math'. 
  EXECUTE.
  COMPUTE mmiirw = mmii1rw + mmii2rw + mmii3rw. 
  VARIABLE LABELS  mmiirw '# of correct answers from all problems in interest instructional level math'. 
  EXECUTE.
  COMPUTE mmbmrw = mmbm1rw + mmbm2rw + mmbm3rw. 
  VARIABLE LABELS  mmbmrw '# of correct answers from all problems in boring mastery level math'. 
  EXECUTE.
  COMPUTE mmbirw = mmbi1rw + mmbi2rw + mmbi3rw . 
  VARIABLE LABELS  mmbirw '# of correct answers from all problems in boring instructional level math'. 
  EXECUTE.
  """
    
    
    switchtext = "DATASET ACTIVATE main.\n"
    
    f.write("DATASET NAME main.\n")
    
    text1 = """DATASET COPY  mainCopy1 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy1.\n"""
    
    f.write(text1)
    f.write(compute)
    f.write(GLMtext)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy1.\n")
   
   
main()