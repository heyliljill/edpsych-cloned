# 4.(Table 6) mean number of checks, by type, out of 12 problems (pmim1chk pmim2chk pmim3chk pmii1chk...) (12 total)
# a.can't tell how checked (=2), checks alternate set-up (=6), checks reasonableness (=5), computational check (=3), no check (=1), operations check (=4)
# b.Break up into interest, difficulty, gender


# pmimchk = pmim1chk + pmim2chk + pmim3chk 
# pmiichk = pmii1chk + pmii2chk + pmii3chk
# pmbmchk = pmbm1chk + pmbm2chk + pmbm3chk
# pmbichk = pmbi1chk + pmbi2chk + pmbi3chk 


f = open('manova-checks','w+')

def main():
  
  GLMtext = """
GLM pmimchk pmiichk pmbmchk pmbichk BY sex
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
  
  compute = """COMPUTE pmimchk = pmim1chk + pmim2chk + pmim3chk. 
VARIABLE LABELS  pmimchk '# of checks from all problems in interest mastery level math'. 
EXECUTE.
COMPUTE pmiichk = pmii1chk + pmii2chk + pmii3chk. 
VARIABLE LABELS  pmiichk '# of checks from all problems in interest instructional level math'. 
EXECUTE.
COMPUTE pmbmchk = pmbm1chk + pmbm2chk + pmbm3chk. 
VARIABLE LABELS  pmbmchk '# of checks from all problems in boring mastery level math'. 
EXECUTE.
COMPUTE pmbichk = pmbi1chk + pmbi2chk + pmbi3chk . 
VARIABLE LABELS  pmbichk '# of checks from all problems in boring instructional level math'. 
EXECUTE.
"""
  
  
  switchtext = "DATASET ACTIVATE main.\n"
  
  f.write("DATASET NAME main.\n")
  
  text1 = """DATASET COPY  mainCopy1 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy1.\n"""
  
  f.write(text1)
  f.write("recode mmim1chk mmii1chk mmbm1chk mmbi1chk mmim2chk mmii2chk mmbm2chk mmbi2chk mmim3chk mmii3chk mmbm3chk mmbi3chk (1=1) (else = 0).\n")
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy1.\n")
    
  text2 = """DATASET COPY  mainCopy2 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy2.\n"""

  f.write(text2)
  f.write("recode mmim1chk mmii1chk mmbm1chk mmbi1chk mmim2chk mmii2chk mmbm2chk mmbi2chk mmim3chk mmii3chk mmbm3chk mmbi3chk (2=1) (else = 0).\n")
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy2.\n")
      
  text3 = """DATASET COPY  mainCopy3 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy3.\n"""

  f.write(text3)
  f.write("recode mmim1chk mmii1chk mmbm1chk mmbi1chk mmim2chk mmii2chk mmbm2chk mmbi2chk mmim3chk mmii3chk mmbm3chk mmbi3chk (3=1) (else = 0).\n")
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy3.\n")
      
  text4 = """DATASET COPY  mainCopy4 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy4.\n"""

  f.write(text4)
  f.write("recode mmim1chk mmii1chk mmbm1chk mmbi1chk mmim2chk mmii2chk mmbm2chk mmbi2chk mmim3chk mmii3chk mmbm3chk mmbi3chk (4=1) (else = 0).\n")
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy4.\n")

  text5 = """DATASET COPY  mainCopy5 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy5.\n"""

  f.write(text5)
  f.write("recode mmim1chk mmii1chk mmbm1chk mmbi1chk mmim2chk mmii2chk mmbm2chk mmbi2chk mmim3chk mmii3chk mmbm3chk mmbi3chk (5=1) (else = 0).\n")
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy5.\n")

  text6 = """DATASET COPY  mainCopy6 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy6.\n"""
  
  f.write(text6)
  f.write("recode mmim1chk mmii1chk mmbm1chk mmbi1chk mmim2chk mmii2chk mmbm2chk mmbi2chk mmim3chk mmii3chk mmbm3chk mmbi3chk (6=1) (else = 0).\n")
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy6.\n")
  
  
main()