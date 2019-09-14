# 3.	(Table 5) mean number of mistakes, by type, out of 12 problems (mmim1mis, mmim2mis, mmmim3mis... 12 total)
# a.	a.	computational (=4), copying (=5), partial set-up ( =2), set-up (=1), unattempted (=6), unfinished (=3)
# b.	Break up into interest, difficulty, gender


# mmimmis = mmim1mis + mmim2mis + mmim3mis 
# mmiimis = mmii1mis + mmii2mis + mmii3mis
# mmbmmis = mmbm1mis + mmbm2mis + mmbm3mis
# mmbimis = mmbi1mis + mmbi2mis + mmbi3mis 


f = open('manova-mistakes','w+')

def computeLine(variable):
  prefix=variable[0:2]
  level=variable[2:4]
  suffix=variable[4:]
  sum = prefix+level+suffix
  first = prefix+level+'1'+suffix
  second = prefix+level+'2'+suffix
  third = prefix+level+'3'+suffix
  computeLines ="""COMPUTE """+sum+""" = """+first+""" + """+second+""" + """+third+""".
VARIABLE LABELS  """+ sum+""" '# of mistakes of this type made in """+level+""" level math'. 
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

def recode(prefix,suffix,num):
  levels = ["im","ii","bm","bi"]
  vars = ""
  for level in levels:
    for i in range(1,4):
      vars = vars+prefix+level+str(i)+suffix+" "
  recodetext= "recode "+vars+"("+str(num)+"=1) (else = 0).\n"
  return recodetext

def main():
  
  prefix = "mm"
  suffix = "mis"
  
  intmast = prefix+"im"+suffix+" "
  intinst = prefix+"ii"+suffix+" "
  boringmast = prefix+"bm"+suffix+" "
  boringinst = prefix+"bi"+suffix+" "
  
  domain = "mathspint"
  
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
  
  f.write(makeCopy(1))
  f.write(recode("mm","mis",1))
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(1))
  
  f.write(makeCopy(2))
  f.write(recode("mm","mis",2))
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(2))
 
  f.write(makeCopy(3))
  f.write(recode("mm","mis",3))
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(3))
 
  f.write(makeCopy(4))
  f.write(recode("mm","mis",4))
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(4))
  
  f.write(makeCopy(5))
  f.write(recode("mm","mis",5))
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(5))  

  f.write(makeCopy(6))
  f.write(recode("mm","mis",6))
  f.write(compute)
  f.write(GLMtext)
  f.write(switchtext)
  f.write(closeCopy(6))

main()