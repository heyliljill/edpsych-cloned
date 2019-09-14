# 5.	(Table 7) Mean number of paragraphs represented in reading, per passage (3 paragraphs) (mrimpara,mriipara...4 total)
# a.	3 paragraphs (=3), 2 paragraphs (=2), 1 paragraph (=1), topic only (=4), topic related (=5) 
# b.	Break up into interest, difficulty, gender
# c.	By overall, WDI - Reading subsample, LWDI - Reading subsample

f = open('manova-paragraphs','w+')

def main():
  
  GLMtext = """
GLM mrimpara mriipara mrbmpara mrbipara BY sex
  /WSFACTOR=interest 2 Polynomial diff 2 Polynomial 
  /METHOD=SSTYPE(3) :
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

recode mrimpara mriipara mrbmpara mrbipara (1=1) (else = 0)."""
  
  f.write(text1)
  f.write(GLMtext)
  f.write(switchtext)
    
  text2 = """DATASET COPY  mainCopy2 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy2.\n

recode mrimpara mriipara mrbmpara mrbipara (2=1) (else = 0)."""
  
  f.write(text2)
  f.write(GLMtext)
  f.write(switchtext)
      
  text3 = """DATASET COPY  mainCopy3 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy3.\n

recode mrimpara mriipara mrbmpara mrbipara (3=1) (else = 0)."""
  
  f.write(text3)
  f.write(GLMtext)
  f.write(switchtext)
      
  text4 = """DATASET COPY  mainCopy4 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy4.\n

recode mrimpara mriipara mrbmpara mrbipara (4=1) (else = 0)."""
  
  f.write(text4)
  f.write(GLMtext)
  f.write(switchtext)
      
  text5 = """DATASET COPY  mainCopy5 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy5.\n

recode mrimpara mriipara mrbmpara mrbipara (5=1) (else = 0)."""
  
  f.write(text5)
  f.write(GLMtext)
  f.write(switchtext)
  
main()