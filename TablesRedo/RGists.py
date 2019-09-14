# 4.	(Table 6) Mean number of Overall gists employed in reading, per passage (3 paragraphs) (mrimgist, mriigist... 4 total)
# a.	Full gist (=3), 2-part relation gist (=5), partial gist (=1), 2 parts(=2), half-gist (=4), no gist (=0)
# b.	Break up into interest, difficulty, gender
# c.	By overall, WDI - Reading subsample, LWDI - Reading subsample

f = open('manova-gists','w+')

def main():
  
  GLMtext = """
GLM mrimgist mriigist mrbmgist mrbigist BY sex
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

recode mrimgist mriigist mrbmgist mrbigist (1=1) (else = 0)."""
  
  f.write(text1)
  f.write(GLMtext)
  f.write(switchtext)
    
  text2 = """DATASET COPY  mainCopy2 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy2.\n

recode mrimgist mriigist mrbmgist mrbigist (2=1) (else = 0)."""
  
  f.write(text2)
  f.write(GLMtext)
  f.write(switchtext)
      
  text3 = """DATASET COPY  mainCopy3 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy3.\n

recode mrimgist mriigist mrbmgist mrbigist (3=1) (else = 0)."""
  
  f.write(text3)
  f.write(GLMtext)
  f.write(switchtext)
      
  text4 = """DATASET COPY  mainCopy4 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy4.\n

recode mrimgist mriigist mrbmgist mrbigist (4=1) (else = 0)."""
  
  f.write(text4)
  f.write(GLMtext)
  f.write(switchtext)
      
  text5 = """DATASET COPY  mainCopy5 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy5.\n

recode mrimgist mriigist mrbmgist mrbigist (5=1) (else = 0)."""
  
  f.write(text5)
  f.write(GLMtext)
  f.write(switchtext)
  
  text6 = """DATASET COPY  mainCopy6 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy6.\n

recode mrimgist mriigist mrbmgist mrbigist (6=1) (else = 0)."""
  
  f.write(text6)
  f.write(GLMtext)
  f.write(switchtext)
  
main()