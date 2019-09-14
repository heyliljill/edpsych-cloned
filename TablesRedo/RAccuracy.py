#6.	(Table 8) Means for levels of accuracy in reading, per passage (3 paragraphs) (mrimacc,mriiacc...4 total)
#a.	Accurate and complete (=3), accurate not complete (=4), concepts correct/factual mistakes (=3), largely inaccurate (=1)
#b.	Break up into interest, difficulty, gender
#c.	By overall, WDI - Reading subsample, LWDI - Reading subsample



f = open('manova-accuracy','w+')

def main():
  
  GLMtext = """
GLM mrimacc mriiacc mrbmacc mrbiacc BY sex
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
  switchtext = "DATASET ACTIVATE main.\n"
  
  f.write("DATASET NAME main.\n")
  
  text1 = """DATASET COPY  mainCopy1 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy1.\n

recode mrimacc mriiacc mrbmacc mrbiacc (1=1) (else = 0)."""
  
  f.write(text1)
  f.write(GLMtext)
  f.write(switchtext)
    
  text2 = """DATASET COPY  mainCopy2 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy2.\n

recode mrimacc mriiacc mrbmacc mrbiacc (2=1) (else = 0)."""
  
  f.write(text2)
  f.write(GLMtext)
  f.write(switchtext)
      
  text3 = """DATASET COPY  mainCopy3 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy3.\n

recode mrimacc mriiacc mrbmacc mrbiacc (3=1) (else = 0)."""
  
  f.write(text3)
  f.write(GLMtext)
  f.write(switchtext)
      
  text4 = """DATASET COPY  mainCopy4 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy4.\n

recode mrimacc mriiacc mrbmacc mrbiacc (4=1) (else = 0)."""
  
  f.write(text4)
  f.write(GLMtext)

  
main()