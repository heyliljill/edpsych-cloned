# Labels, by type, out of 12 problems 
# 	a. (mmim1lb1, mmim2lb1, mmmim3lb1... 12 total). Unit in label. none = 0, correct = 1, incorrect = 2, variation = 3, interpretation = 4 
#   b. (mmim1lb2, mmim2lb2, mmmim3lb2... 12 total). Context of label. none = 0, minimal = 1, full = 2, incorrect = 3, general = 4
#   c. (mmim1lb3, mmim2lb3, mmmim3lb3... 12 total). Sentence for label. no = 0, yes = 1. 

# b.	Break up into interest, difficulty, gender

# mmimlb1 = mmim1lb1 + mmim2lb1 + mmim3lb1 
# mmiilb1 = mmii1lb1 + mmii2lb1 + mmii3lb1
# mmbmlb1 = mmbm1lb1 + mmbm2lb1 + mmbm3lb1
# mmbilb1 = mmbi1lb1 + mmbi2lb1 + mmbi3lb1 

# mmimlb2 = mmim1lb2 + mmim2lb2 + mmim3lb2 
# mmiilb2 = mmii1lb2 + mmii2lb2 + mmii3lb2
# mmbmlb2 = mmbm1lb2 + mmbm2lb2 + mmbm3lb2
# mmbilb2 = mmbi1lb2 + mmbi2lb2 + mmbi3lb2 

# mmimlb3 = mmim1lb3 + mmim2lb3 + mmim3lb3 
# mmiilb3 = mmii1lb3 + mmii2lb3 + mmii3lb3
# mmbmlb3 = mmbm1lb3 + mmbm2lb3 + mmbm3lb3
# mmbilb3 = mmbi1lb3 + mmbi2lb3 + mmbi3lb3 



f = open('manova-labelsSPINT','w+')

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

    GLMtext_lb1 = """
  GLM mmimlb1 mmiilb1 mmbmlb1 mmbilb1 BY sex
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
    
    GLMtext_lb2 = """
  GLM mmimlb2 mmiilb2 mmbmlb2 mmbilb2 BY sex
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
    
    GLMtext_lb3 = """
  GLM mmimlb3 mmiilb3 mmbmlb3 mmbilb3 BY sex
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
    
    
    
    
    compute_lb1 = """COMPUTE mmimlb1=mmim1lb1 + mmim2lb1 + mmim3lb1. 
  VARIABLE LABELS  mmimlb1 'unit labels from all paragraphs in interest mastery level reading recall'. 
  EXECUTE.
  COMPUTE mmiilb1=mmii1lb1 + mmii2lb1 + mmii3lb1. 
  VARIABLE LABELS  mmiilb1 'unit labels from all paragraphs in interest instructional level reading recall'. 
  EXECUTE.
  COMPUTE mmbmlb1=mmbm1lb1 + mmbm2lb1 + mmbm3lb1. 
  VARIABLE LABELS  mmbmlb1 'unit labels from all paragraphs in boring mastery level reading recall'. 
  EXECUTE.
  COMPUTE mmbilb1=mmbi1lb1 + mmbi2lb1 + mmbi3lb1. 
  VARIABLE LABELS  mmbilb1 'unit labels from all paragraphs in boring instructional level reading recall'. 
  EXECUTE.
  """
  
    compute_lb2 = """COMPUTE mmimlb2=mmim1lb2 + mmim2lb2 + mmim3lb2. 
  VARIABLE LABELS  mmimlb2 'context of labels in all paragraphs in interest mastery level reading recall'. 
  EXECUTE.
  COMPUTE mmiilb2=mmii1lb2 + mmii2lb2 + mmii3lb2. 
  VARIABLE LABELS  mmiilb2 'context of labels in all paragraphs in interest instructional level reading recall'. 
  EXECUTE.
  COMPUTE mmbmlb2=mmbm1lb2 + mmbm2lb2 + mmbm3lb2. 
  VARIABLE LABELS  mmbmlb2 'context of labels in all paragraphs in boring mastery level reading recall'. 
  EXECUTE.
  COMPUTE mmbilb2=mmbi1lb2 + mmbi2lb2 + mmbi3lb2. 
  VARIABLE LABELS  mmbilb2 'context of labels in all paragraphs in boring instructional level reading recall'. 
  EXECUTE.
  """
  
    compute_lb3 = """COMPUTE mmimlb3=mmim1lb3 + mmim2lb3 + mmim3lb3. 
  VARIABLE LABELS  mmimlb3 'sentence from label in all paragraphs in interest mastery level reading recall'. 
  EXECUTE.
  COMPUTE mmiilb3=mmii1lb3 + mmii2lb3 + mmii3lb3. 
  VARIABLE LABELS  mmiilb3 'sentence from label in all paragraphs in interest instructional level reading recall'. 
  EXECUTE.
  COMPUTE mmbmlb3=mmbm1lb3 + mmbm2lb3 + mmbm3lb3. 
  VARIABLE LABELS  mmbmlb3 'sentence from label in all paragraphs in boring mastery level reading recall'. 
  EXECUTE.
  COMPUTE mmbilb3=mmbi1lb3 + mmbi2lb3 + mmbi3lb3. 
  VARIABLE LABELS  mmbilb3 'sentence from label in all paragraphs in boring instructional level reading recall'. 
  EXECUTE.
  """
  
  
    
    switchtext = "DATASET ACTIVATE main.\n"
    
    f.write("DATASET NAME main.\n")
  
    ## lb1 ##
  
    text0 = """DATASET COPY  mainCopy0 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy0.\n
    
  recode mmim1lb1 mmii1lb1 mmbm1lb1 mmbi1lb1 (0=1) (else = 0).
  recode mmim2lb1 mmii2lb1 mmbm2lb1 mmbi2lb1 (0=1) (else = 0).
  recode mmim3lb1 mmii3lb1 mmbm3lb1 mmbi3lb1 (0=1) (else = 0).\n"""
    
    f.write(text0)
    f.write(compute_lb1)
    f.write(GLMtext_lb1)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy0.\n")
    
    text1 = """DATASET COPY  mainCopy1 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy1.\n
    
  recode mmim1lb1 mmii1lb1 mmbm1lb1 mmbi1lb1 (1=1) (else = 0).
  recode mmim2lb1 mmii2lb1 mmbm2lb1 mmbi2lb1 (1=1) (else = 0).
  recode mmim3lb1 mmii3lb1 mmbm3lb1 mmbi3lb1 (1=1) (else = 0).\n"""
    
    f.write(text1)
    f.write(compute_lb1)
    f.write(GLMtext_lb1)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy1.\n")
  
    text2 = """DATASET COPY  mainCopy2 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy2.\n
    
  recode mmim1lb1 mmii1lb1 mmbm1lb1 mmbi1lb1 (2=1) (else = 0).
  recode mmim2lb1 mmii2lb1 mmbm2lb1 mmbi2lb1 (2=1) (else = 0).
  recode mmim3lb1 mmii3lb1 mmbm3lb1 mmbi3lb1 (2=1) (else = 0).\n"""
    
    
    f.write(text2)
    f.write(compute_lb1)
    f.write(GLMtext_lb1)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy2.\n")
        
    text3 = """DATASET COPY  mainCopy3 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy3.\n
    
  recode mmim1lb1 mmii1lb1 mmbm1lb1 mmbi1lb1 (3=1) (else = 0).
  recode mmim2lb1 mmii2lb1 mmbm2lb1 mmbi2lb1 (3=1) (else = 0).
  recode mmim3lb1 mmii3lb1 mmbm3lb1 mmbi3lb1 (3=1) (else = 0).\n"""
  
  
    f.write(text3)
    f.write(compute_lb1)
    f.write(GLMtext_lb1)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy3.\n")
  
    text4 = """DATASET COPY  mainCopy4 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy4.\n
    
  recode mmim1lb1 mmii1lb1 mmbm1lb1 mmbi1lb1 (4=1) (else = 0).
  recode mmim2lb1 mmii2lb1 mmbm2lb1 mmbi2lb1 (4=1) (else = 0).
  recode mmim3lb1 mmii3lb1 mmbm3lb1 mmbi3lb1 (4=1) (else = 0).\n"""
  
    f.write(text4)
    f.write(compute_lb1)
    f.write(GLMtext_lb1)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy4.\n")  
    
  
    ## lb2 ##
  
    text05 = """DATASET COPY  mainCopy05 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy05.\n
    
  recode mmim1lb2 mmii1lb2 mmbm1lb2 mmbi1lb2 (0=1) (else = 0).
  recode mmim2lb2 mmii2lb2 mmbm2lb2 mmbi2lb2 (0=1) (else = 0).
  recode mmim3lb2 mmii3lb2 mmbm3lb2 mmbi3lb2 (0=1) (else = 0).\n"""
    
    f.write(text05)
    f.write(compute_lb2)
    f.write(GLMtext_lb2)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy05.\n")  
    
    text5 = """DATASET COPY  mainCopy5 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy5.\n
    
  recode mmim1lb2 mmii1lb2 mmbm1lb2 mmbi1lb2 (1=1) (else = 0).
  recode mmim2lb2 mmii2lb2 mmbm2lb2 mmbi2lb2 (1=1) (else = 0).
  recode mmim3lb2 mmii3lb2 mmbm3lb2 mmbi3lb2 (1=1) (else = 0).\n"""
    
    f.write(text5)
    f.write(compute_lb2)
    f.write(GLMtext_lb2)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy5.\n")
  
    text6 = """DATASET COPY  mainCopy6 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy6.\n
    
  recode mmim1lb2 mmii1lb2 mmbm1lb2 mmbi1lb2 (2=1) (else = 0).
  recode mmim2lb2 mmii2lb2 mmbm2lb2 mmbi2lb2 (2=1) (else = 0).
  recode mmim3lb2 mmii3lb2 mmbm3lb2 mmbi3lb2 (2=1) (else = 0).\n"""
    
    f.write(text6)
    f.write(compute_lb2)
    f.write(GLMtext_lb2)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy6.\n")
        
    text7 = """DATASET COPY  mainCopy7 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy7.\n
    
  recode mmim1lb2 mmii1lb2 mmbm1lb2 mmbi1lb2 (3=1) (else = 0).
  recode mmim2lb2 mmii2lb2 mmbm2lb2 mmbi2lb2 (3=1) (else = 0).
  recode mmim3lb2 mmii3lb2 mmbm3lb2 mmbi3lb2 (3=1) (else = 0).\n"""
  
    f.write(text7)
    f.write(compute_lb2)
    f.write(GLMtext_lb2)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy7.\n")
  
    text8 = """DATASET COPY  mainCopy8 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy8.\n
    
  recode mmim1lb2 mmii1lb2 mmbm1lb2 mmbi1lb2 (4=1) (else = 0).
  recode mmim2lb2 mmii2lb2 mmbm2lb2 mmbi2lb2 (4=1) (else = 0).
  recode mmim3lb2 mmii3lb2 mmbm3lb2 mmbi3lb2 (4=1) (else = 0).\n"""
  
    f.write(text8)
    f.write(compute_lb2)
    f.write(GLMtext_lb2)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy8.\n")  
  
  
    ## lb3 ##
    
    text9 = """DATASET COPY  mainCopy9 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy9.\n"""
    
    f.write(text9)
    f.write(compute_lb3)
    f.write(GLMtext_lb3)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy9.\n")


    
  
main()