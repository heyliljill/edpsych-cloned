# 3.	(Table 5) Mean scores for content and form in Reading, per passage (3 paragraphs)
# a.	Points remembered (mrim1p, mrim2p,mrim3p, mrii1p... 12 total), Gists recalled (mrim1g, mrim2g,mrim3g, mrii1g... 12 total), Sentences written (mrimsent,mriisent...4 total), Paragraphs represented (mrimpara,mriipara...4 total),
# b.	Break up into interest, difficulty, gender
# c.	By overall, WDI - Reading subsample, LWDI - Reading subsample

## computing points and gists

# mrimp = mrim1p + mrim2p + mrim3p 
# mriip = mrii1p + mrii2p + mrii3p
# mrbmp = mrbm1p + mrbm2p + mrbm3p
# mrbip = mrbi1p + mrbi2p + mrbi3p 

# mrimg = mrim1g + mrim2g + mrim3g 
# mriig = mrii1g + mrii2g + mrii3g
# mrbmg = mrbm1g + mrbm2g + mrbm3g
# mrbig = mrbi1g + mrbi2g + mrbi3g 

# mrimsent mriisent mrbmsent mrbisent

# paragraphs : recode 1 = 1, 2 = 2, 3 = 3, else = 0. 1 corresponds to 1 paragraph, etc. 



f = open('manova-contentform','w+')

def main():

  GLMtext_p = """
GLM mrimp mriip mrbmp mrbip BY sex
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
  
  GLMtext_g = """
GLM mrimg mriig mrbmg mrbig BY sex
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
  
  GLMtext_sent = """
GLM mrimsent mriisent mrbmsent mrbisent BY sex
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
  
  
  GLMtext_para = """
GLM mrimpara mriipara mrbmpara mrbipara BY sex
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
  
  
  
  
  compute_p = """COMPUTE mrimp=mrim1p + mrim2p + mrim3p. 
VARIABLE LABELS  mrimp '# of points from all paragraphs in interest mastery level reading recall'. 
EXECUTE.
COMPUTE mriip=mrii1p + mrii2p + mrii3p. 
VARIABLE LABELS  mriip '# of points from all paragraphs in interest instructional level reading recall'. 
EXECUTE.
COMPUTE mrbmp=mrbm1p + mrbm2p + mrbm3p. 
VARIABLE LABELS  mrbmp '# of points from all paragraphs in boring mastery level reading recall'. 
EXECUTE.
COMPUTE mrbip=mrbi1p + mrbi2p + mrbi3p. 
VARIABLE LABELS  mrbip '# of points from all paragraphs in boring instructional level reading recall'. 
EXECUTE.
"""
  compute_g = """COMPUTE mrimg=mrim1g + mrim2g + mrim3g. 
VARIABLE LABELS  mrimg '# of gists from all paragraphs in interest mastery level reading recall'. 
EXECUTE.
COMPUTE mriig=mrii1g + mrii2g + mrii3g. 
VARIABLE LABELS  mriig '# of gists from all paragraphs in interest instructional level reading recall'. 
EXECUTE.
COMPUTE mrbmg=mrbm1g + mrbm2g + mrbm3g. 
VARIABLE LABELS  mrbmg '# of gists from all paragraphs in boring mastery level reading recall'. 
EXECUTE.
COMPUTE mrbig=mrbi1g + mrbi2g + mrbi3g. 
VARIABLE LABELS  mrbig '# of gists from all paragraphs in boring instructional level reading recall'. 
EXECUTE.
"""


  
  switchtext = "DATASET ACTIVATE main.\n"
  
  f.write("DATASET NAME main.\n")
  
  ## POINTS ##
  
  text1 = """DATASET COPY  mainCopy1 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy1.\n"""
  
  f.write(text1)
  f.write(compute_p)
  f.write(GLMtext_p)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy1.\n")
    
  text2 = """DATASET COPY  mainCopy2 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy2.\n"""
  
  ## GISTS ##
  
  f.write(text2)
  f.write(compute_g)
  f.write(GLMtext_g)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy2.\n")
      
  text3 = """DATASET COPY  mainCopy3 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy3.\n"""
  
  ## SENTENCES ##
  
  f.write(text3)
  f.write(GLMtext_sent)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy3.\n")
  
  text4 = """DATASET COPY  mainCopy4 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy4.
  
recode mrimpara mriipara mrbmpara mrbipara (1=1) (2=2) (3=3) (else = 0).\n"""
  
  ## PARAGRAPHS ##

  f.write(text4)
  f.write(GLMtext_para)
  f.write(switchtext)
  f.write("DATASET CLOSE mainCopy4.\n")
  
  
main()