# 7.	(Table 9) Means for types of distortions in reading, per passage (3 paragraphs)
# a.	Misread (=3), misunderstood (=7), misremembered (=4), miscombined (=2), mislabeled (=6), included extraneous information (=1), added information, elaborated on text (=10), comments on text (=11)

## IDEA: DO mrimsub1 recode them level by level (like 1=1..2=1...) then do same for mrimsub2. for each level, combine them somehow?
## Total will never be more than 1. So take sum of sub1 and sub2. Then do GLM on it.


f = open('manova-distortionsSPINT','w+')

def main():
  
  mathread = "r"
  
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
  GLM mrimsub mriisub mrbmsub mrbisub BY sex
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
    
    compute = """\ncompute mrimsub = mrimsub1 + mrimsub2.
  compute mriisub = mriisub1 + mriisub2.
  compute mrbmsub = mrbmsub1 + mrbmsub2.
  compute mrbisub = mrbisub1 + mrbisub2.
  """
    
    switchtext = "DATASET ACTIVATE main.\n"
    
    f.write("DATASET NAME main.\n")
    
    text1 = """DATASET COPY  mainCopy1 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy1.\n
    
  recode mrimsub1 mriisub1 mrbmsub1 mrbisub1 (1=1) (else = 0).
  recode mrimsub2 mriisub2 mrbmsub2 mrbisub2 (1=1) (else = 0)."""
    
    f.write(text1)
    f.write(compute)
    f.write(GLMtext)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy1.\n")
      
    text2 = """DATASET COPY  mainCopy2 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy2.\n
  
  recode mrimsub1 mriisub1 mrbmsub1 mrbisub1 (2=1) (else = 0).
  recode mrimsub2 mriisub2 mrbmsub2 mrbisub2 (2=1) (else = 0)."""
    
    f.write(text2)
    f.write(compute)
    f.write(GLMtext)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy2.\n")
        
    text3 = """DATASET COPY  mainCopy3 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy3.\n
  
  recode mrimsub1 mriisub1 mrbmsub1 mrbisub1 (3=1) (else = 0).
  recode mrimsub2 mriisub2 mrbmsub2 mrbisub2 (3=1) (else = 0)."""
    
    f.write(text3)
    f.write(compute)
    f.write(GLMtext)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy3.\n")
        
    text4 = """DATASET COPY  mainCopy4 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy4.\n
  
  recode mrimsub1 mriisub1 mrbmsub1 mrbisub1 (4=1) (else = 0).
  recode mrimsub2 mriisub2 mrbmsub2 mrbisub2 (4=1) (else = 0)."""
    
    f.write(text4)
    f.write(compute)
    f.write(GLMtext)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy4.\n")
        
    text5 = """DATASET COPY  mainCopy5 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy5.\n
  
  recode mrimsub1 mriisub1 mrbmsub1 mrbisub1 (5=1) (else = 0).
  recode mrimsub2 mriisub2 mrbmsub2 mrbisub2 (5=1) (else = 0)."""
    
    f.write(text5)
    f.write(compute)
    f.write(GLMtext)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy5.\n")
  
    text6 = """DATASET COPY  mainCopy6 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy6.\n
  
  recode mrimsub1 mriisub1 mrbmsub1 mrbisub1 (6=1) (else = 0).
  recode mrimsub2 mriisub2 mrbmsub2 mrbisub2 (6=1) (else = 0)."""
    
    f.write(text6)
    f.write(compute)
    f.write(GLMtext)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy6.\n")
    
    text7 = """DATASET COPY  mainCopy7 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy7.\n
  
  recode mrimsub1 mriisub1 mrbmsub1 mrbisub1 (7=1) (else = 0).
  recode mrimsub2 mriisub2 mrbmsub2 mrbisub2 (7=1) (else = 0)."""
    
    f.write(text7)
    f.write(compute)
    f.write(GLMtext)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy7.\n")
  
    text8 = """DATASET COPY  mainCopy8 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy8.\n
  
  recode mrimsub1 mriisub1 mrbmsub1 mrbisub1 (8=1) (else = 0).
  recode mrimsub2 mriisub2 mrbmsub2 mrbisub2 (8=1) (else = 0)."""
    
    f.write(text8)
    f.write(compute)
    f.write(GLMtext)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy8.\n")
    
    text10 = """DATASET COPY  mainCopy10 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy10.\n
  
  recode mrimsub1 mriisub1 mrbmsub1 mrbisub1 (10=1) (else = 0).
  recode mrimsub2 mriisub2 mrbmsub2 mrbisub2 (10=1) (else = 0)."""
    
    f.write(text10)
    f.write(compute)
    f.write(GLMtext)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy10.\n")
    
    text11 = """DATASET COPY  mainCopy11 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy11.\n
  
  recode mrimsub1 mriisub1 mrbmsub1 mrbisub1 (11=1) (else = 0).
  recode mrimsub2 mriisub2 mrbmsub2 mrbisub2 (11=1) (else = 0)."""
    
    f.write(text11)
    f.write(compute)
    f.write(GLMtext)
    f.write(switchtext)
    f.write("DATASET CLOSE mainCopy11.\n")
    

  

main()