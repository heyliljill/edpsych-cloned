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

def computeLine(variable):
  prefix=variable[0:2]
  level=variable[2:4]
  suffix=variable[4:6]
  sum = prefix+level+suffix
  first = prefix+level+'1'+suffix
  second = prefix+level+'2'+suffix
  third = prefix+level+'3'+suffix
  computeLines ="""COMPUTE """+sum+""" = """+first+""" + """+second+""" + """+third+""".
VARIABLE LABELS  """+ sum+""" '# of """+suffix+""" represented in """+level+""" level reading'. 
EXECUTE.
"""
  return computeLines

def makeCopy(int):
  num = str(int)
  text = "DATASET COPY  mainCopy"+num+" WINDOW=FRONT.\nDATASET ACTIVATE mainCopy"+num+".\n"
  return text
  
def closeCopy(int):
  num = str(int)
  text = "DATASET CLOSE mainCopy"+num+".\n"
  return text
  

def recodepara(prefix,suffix):
  levels = ["im","ii","bm","bi"]
  vars = ""
  for level in levels:
    vars = vars+prefix+level+suffix+" "
  recodetext= "recode "+vars+"(1=1) (2=2) (3=3) (else = 0).\n"
  return recodetext

def main():
  
  prefix = "mr"
  suffix = "p"
  
  intmast = prefix+"im"+suffix+" "
  intinst = prefix+"ii"+suffix+" "
  boringmast = prefix+"bm"+suffix+" "
  boringinst = prefix+"bi"+suffix+" "
  
  domain = "readspint"
  
  filteron ="""USE ALL. 
COMPUTE filter_$=(group = 1  & int = 0). 
VARIABLE LABELS filter_$ 'group = 1  & int = 0 (FILTER)'. 
VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. 
FORMATS filter_$ (f1.0). 
FILTER BY filter_$. 
EXECUTE.
"""

  
  GLMtext = """GLM """+intmast+intinst+boringmast+boringinst+ """ BY """+ domain +""" sex 
/WSFACTOR=interest 2 Polynomial difficulty 2 Polynomial 
/METHOD=SSTYPE(3) 
/EMMEANS=TABLES(OVERALL) 
/EMMEANS=TABLES("""+domain+""") COMPARE ADJ(LSD) 
/EMMEANS=TABLES(sex) COMPARE ADJ(LSD) 
/EMMEANS=TABLES(interest) COMPARE ADJ(LSD) 
/EMMEANS=TABLES(difficulty) COMPARE ADJ(LSD) 
/EMMEANS=TABLES("""+domain+"""*sex) 
/EMMEANS=TABLES("""+domain+"""*interest) 
/EMMEANS=TABLES("""+domain+"""*difficulty) 
/EMMEANS=TABLES(sex*interest) 
/EMMEANS=TABLES(sex*difficulty) 
/EMMEANS=TABLES(interest*difficulty) 
/EMMEANS=TABLES("""+domain+"""*sex*interest) 
/EMMEANS=TABLES("""+domain+"""*sex*difficulty) 
/EMMEANS=TABLES("""+domain+"""*interest*difficulty) 
/EMMEANS=TABLES(sex*interest*difficulty) 
/EMMEANS=TABLES("""+domain+"""*sex*interest*difficulty)
/PRINT=DESCRIPTIVE
/CRITERIA=ALPHA(.05) 
/WSDESIGN=interest difficulty interest*difficulty 
/DESIGN="""+domain+""" sex """+domain+"""*sex.
  """

  compute = computeLine(intmast) + computeLine(intinst) + computeLine(boringmast) + computeLine(boringinst)
  
  switchtext = "DATASET ACTIVATE main.\n"
  
  f.write("DATASET NAME main.\n")
  f.write(filteron)
  
  ## POINTS ##
  
  f.write(makeCopy(1))
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(1))
  
  ## GISTS ##
  
  suffix = "g"
  
  intmast = prefix+"im"+suffix+" "
  intinst = prefix+"ii"+suffix+" "
  boringmast = prefix+"bm"+suffix+" "
  boringinst = prefix+"bi"+suffix+" "
  
  GLMtext = """GLM """+intmast+intinst+boringmast+boringinst+ """ BY """+ domain +""" sex 
/WSFACTOR=interest 2 Polynomial difficulty 2 Polynomial 
/METHOD=SSTYPE(3) 
/EMMEANS=TABLES(OVERALL) 
/EMMEANS=TABLES("""+domain+""") COMPARE ADJ(LSD) 
/EMMEANS=TABLES(sex) COMPARE ADJ(LSD) 
/EMMEANS=TABLES(interest) COMPARE ADJ(LSD) 
/EMMEANS=TABLES(difficulty) COMPARE ADJ(LSD) 
/EMMEANS=TABLES("""+domain+"""*sex) 
/EMMEANS=TABLES("""+domain+"""*interest) 
/EMMEANS=TABLES("""+domain+"""*difficulty) 
/EMMEANS=TABLES(sex*interest) 
/EMMEANS=TABLES(sex*difficulty) 
/EMMEANS=TABLES(interest*difficulty) 
/EMMEANS=TABLES("""+domain+"""*sex*interest) 
/EMMEANS=TABLES("""+domain+"""*sex*difficulty) 
/EMMEANS=TABLES("""+domain+"""*interest*difficulty) 
/EMMEANS=TABLES(sex*interest*difficulty) 
/EMMEANS=TABLES("""+domain+"""*sex*interest*difficulty)
/PRINT=DESCRIPTIVE
/CRITERIA=ALPHA(.05) 
/WSDESIGN=interest difficulty interest*difficulty 
/DESIGN="""+domain+""" sex """+domain+"""*sex.
  """

  compute = computeLine(intmast) + computeLine(intinst) + computeLine(boringmast) + computeLine(boringinst)
  
  f.write(makeCopy(2))
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(2))
 
 ## SENTENCES ##
 
  suffix = "sent"
  
  intmast = prefix+"im"+suffix+" "
  intinst = prefix+"ii"+suffix+" "
  boringmast = prefix+"bm"+suffix+" "
  boringinst = prefix+"bi"+suffix+" "
  
  GLMtext = """GLM """+intmast+intinst+boringmast+boringinst+ """ BY """+ domain +""" sex 
/WSFACTOR=interest 2 Polynomial difficulty 2 Polynomial 
/METHOD=SSTYPE(3) 
/EMMEANS=TABLES(OVERALL) 
/EMMEANS=TABLES("""+domain+""") COMPARE ADJ(LSD) 
/EMMEANS=TABLES(sex) COMPARE ADJ(LSD) 
/EMMEANS=TABLES(interest) COMPARE ADJ(LSD) 
/EMMEANS=TABLES(difficulty) COMPARE ADJ(LSD) 
/EMMEANS=TABLES("""+domain+"""*sex) 
/EMMEANS=TABLES("""+domain+"""*interest) 
/EMMEANS=TABLES("""+domain+"""*difficulty) 
/EMMEANS=TABLES(sex*interest) 
/EMMEANS=TABLES(sex*difficulty) 
/EMMEANS=TABLES(interest*difficulty) 
/EMMEANS=TABLES("""+domain+"""*sex*interest) 
/EMMEANS=TABLES("""+domain+"""*sex*difficulty) 
/EMMEANS=TABLES("""+domain+"""*interest*difficulty) 
/EMMEANS=TABLES(sex*interest*difficulty) 
/EMMEANS=TABLES("""+domain+"""*sex*interest*difficulty)
/PRINT=DESCRIPTIVE
/CRITERIA=ALPHA(.05) 
/WSDESIGN=interest difficulty interest*difficulty 
/DESIGN="""+domain+""" sex """+domain+"""*sex.
  """

  f.write(makeCopy(3))
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(3))
 
 ## PARAGRAPHS ##
 
  suffix = "para"
  
  intmast = prefix+"im"+suffix+" "
  intinst = prefix+"ii"+suffix+" "
  boringmast = prefix+"bm"+suffix+" "
  boringinst = prefix+"bi"+suffix+" "
  
  GLMtext = """GLM """+intmast+intinst+boringmast+boringinst+ """ BY """+ domain +""" sex 
/WSFACTOR=interest 2 Polynomial difficulty 2 Polynomial 
/METHOD=SSTYPE(3) 
/EMMEANS=TABLES(OVERALL) 
/EMMEANS=TABLES("""+domain+""") COMPARE ADJ(LSD) 
/EMMEANS=TABLES(sex) COMPARE ADJ(LSD) 
/EMMEANS=TABLES(interest) COMPARE ADJ(LSD) 
/EMMEANS=TABLES(difficulty) COMPARE ADJ(LSD) 
/EMMEANS=TABLES("""+domain+"""*sex) 
/EMMEANS=TABLES("""+domain+"""*interest) 
/EMMEANS=TABLES("""+domain+"""*difficulty) 
/EMMEANS=TABLES(sex*interest) 
/EMMEANS=TABLES(sex*difficulty) 
/EMMEANS=TABLES(interest*difficulty) 
/EMMEANS=TABLES("""+domain+"""*sex*interest) 
/EMMEANS=TABLES("""+domain+"""*sex*difficulty) 
/EMMEANS=TABLES("""+domain+"""*interest*difficulty) 
/EMMEANS=TABLES(sex*interest*difficulty) 
/EMMEANS=TABLES("""+domain+"""*sex*interest*difficulty)
/PRINT=DESCRIPTIVE
/CRITERIA=ALPHA(.05) 
/WSDESIGN=interest difficulty interest*difficulty 
/DESIGN="""+domain+""" sex """+domain+"""*sex.
  """


  f.write(makeCopy(4))
  f.write(recodepara("mr","para"))
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(4))
 
main()