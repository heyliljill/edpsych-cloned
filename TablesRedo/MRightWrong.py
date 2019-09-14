# Math Right Wrong. mean number of correct answers, out of 12 problems (mmim1rw, mmim2rw, mmmim3rw... 12 total)



# mmimrw = mmim1rw + mmim2rw + mmim3rw 
# mmiirw = mmii1rw + mmii2rw + mmii3rw
# mmbmrw = mmbm1rw + mmbm2rw + mmbm3rw
# mmbirw = mmbi1rw + mmbi2rw + mmbi3rw 


f = open('manova-rightwrong','w+')

def main():
  
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