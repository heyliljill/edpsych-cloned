# 3.	(Table 6) Mean number of concurrent verbalizations, per passage ( 3 paraggraphs) Note: look in primoc range of variables. The "overall" slightly differ from the ones in each pargraph. 
# a.	editorial (primoc0d), elaboration (primoc0l), extension (primoc0x), extraneous (primoc0e), incorrect info (prim0ci), gist (primoc0g), point (primoc0p), repeated word (primoc0r)
# b.	Break up into interest, difficulty, gender


f = open('manova-concurrentverb','w+')

def main():
  
  GLMtext = """
GLM primoc0g priioc0g prbmoc0g prbioc0g BY sex
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
  
  text0 = """DATASET COPY  mainCopy0 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy0.\n

recode primoc0g priioc0g prbmoc0g prbioc0g (0=1) (else = 0)."""
  
  f.write(text0)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy0.\n")
  
  text1 = """DATASET COPY  mainCopy1 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy1.\n"

recode primoc0g priioc0g prbmoc0g prbioc0g (1=1) (else = 0)."""
  
  f.write(text1)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy1.\n")
    
  text2 = """DATASET COPY  mainCopy2 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy2.\n

recode primoc0g priioc0g prbmoc0g prbioc0g (2=1) (else = 0)."""
  
  f.write(text2)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy2.\n")
  
  text3 = """DATASET COPY  mainCopy3 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy3.\n

recode primoc0g priioc0g prbmoc0g prbioc0g (3=1) (else = 0)."""
  
  f.write(text3)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy3.\n")
  
  text4 = """DATASET COPY  mainCopy4 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy4.\n

recode primoc0g priioc0g prbmoc0g prbioc0g (4=1) (else = 0)."""
  
  f.write(text4)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy4.\n")
  
  text5 = """DATASET COPY  mainCopy5 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy5.\n

recode primoc0g priioc0g prbmoc0g prbioc0g (5=1) (else = 0)."""
  
  f.write(text5)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy5.\n")  

################################################################################

  f.write("""
  DATASET COPY  mainCopy6 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy6.\n
  
GLM primoc0x priioc0x prbmoc0x prbioc0x BY sex
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
  
  
  GLM primoc0l priioc0l prbmoc0l prbioc0l BY sex
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
  
  
  GLM primoc0e priioc0e prbmoc0e prbioc0e BY sex
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
  
  
  GLM primoc0d priioc0d prbmoc0d prbioc0d BY sex
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
  
  GLM primoc0r priioc0r prbmoc0r prbioc0r BY sex
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
  
  
  GLM primoc0i priioc0i prbmoc0i prbioc0i BY sex
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
    
  

  """)
  f.write("DATASET CLOSE mainCopy6.\n")

 
 
main()