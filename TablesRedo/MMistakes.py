# 3.	(Table 5) mean number of mistakes, by type, out of 12 problems (mmim1mis, mmim2mis, mmmim3mis... 12 total)
# a.	a.	computational (=4), copying (=5), partial set-up ( =2), set-up (=1), unattempted (=6), unfinished (=3)
# b.	Break up into interest, difficulty, gender


# mmimmis = mmim1mis + mmim2mis + mmim3mis 
# mmiimis = mmii1mis + mmii2mis + mmii3mis
# mmbmmis = mmbm1mis + mmbm2mis + mmbm3mis
# mmbimis = mmbi1mis + mmbi2mis + mmbi3mis 


f = open('manova-mistakes','w+')

def main():
  
  GLMtext = """
GLM mmimmis mmiimis mmbmmis mmbimis BY sex
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
  
  compute = """COMPUTE mmimmis = mmim1mis + mmim2mis + mmim3mis. 
VARIABLE LABELS  mmimmis '# of mistakes from all problems in interest mastery level math'. 
EXECUTE.
COMPUTE mmiimis = mmii1mis + mmii2mis + mmii3mis. 
VARIABLE LABELS  mmiimis '# of mistakes from all problems in interest instructional level math'. 
EXECUTE.
COMPUTE mmbmmis = mmbm1mis + mmbm2mis + mmbm3mis. 
VARIABLE LABELS  mmbmmis '# of mistakes from all problems in boring mastery level math'. 
EXECUTE.
COMPUTE mmbimis = mmbi1mis + mmbi2mis + mmbi3mis . 
VARIABLE LABELS  mmbimis '# of mistakes from all problems in boring instructional level math'. 
EXECUTE.
"""
  
  
  switchtext = "DATASET ACTIVATE main.\n"
  
  f.write("DATASET NAME main.\n")
  
  text1 = """DATASET COPY  mainCopy1 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy1.\n"""
  
  f.write(text1)
  f.write("recode mmim1mis mmii1mis mmbm1mis mmbi1mis mmim2mis mmii2mis mmbm2mis mmbi2mis mmim3mis mmii3mis mmbm3mis mmbi3mis (1=1) (else = 0).\n")
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy1.\n")
    
  text2 = """DATASET COPY  mainCopy2 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy2.\n"""

  f.write(text2)
  f.write("recode mmim1mis mmii1mis mmbm1mis mmbi1mis mmim2mis mmii2mis mmbm2mis mmbi2mis mmim3mis mmii3mis mmbm3mis mmbi3mis (2=1) (else = 0).\n")
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy2.\n")
      
  text3 = """DATASET COPY  mainCopy3 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy3.\n"""

  f.write(text3)
  f.write("recode mmim1mis mmii1mis mmbm1mis mmbi1mis mmim2mis mmii2mis mmbm2mis mmbi2mis mmim3mis mmii3mis mmbm3mis mmbi3mis (3=1) (else = 0).\n")
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy3.\n")
      
  text4 = """DATASET COPY  mainCopy4 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy4.\n"""

  f.write(text4)
  f.write("recode mmim1mis mmii1mis mmbm1mis mmbi1mis mmim2mis mmii2mis mmbm2mis mmbi2mis mmim3mis mmii3mis mmbm3mis mmbi3mis (4=1) (else = 0).\n")
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy4.\n")

  text5 = """DATASET COPY  mainCopy5 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy5.\n"""

  f.write(text5)
  f.write("recode mmim1mis mmii1mis mmbm1mis mmbi1mis mmim2mis mmii2mis mmbm2mis mmbi2mis mmim3mis mmii3mis mmbm3mis mmbi3mis (5=1) (else = 0).\n")
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy5.\n")

  text6 = """DATASET COPY  mainCopy6 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy6.\n"""
  
  f.write(text6)
  f.write("recode mmim1mis mmii1mis mmbm1mis mmbi1mis mmim2mis mmii2mis mmbm2mis mmbi2mis mmim3mis mmii3mis mmbm3mis mmbi3mis (6=1) (else = 0).\n")
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy6.\n")
  
main()