## GLM functions

def makeRecodeLine(suffix,proquestions,promain,mathread,stratdiff,nameListi):
  recodevars = []
  for i in range(len(suffix)):
    for j in range(len(proquestions)):
      if (mathread=="r"):
        recodevars.append(promain+mathread+suffix[i]+stratdiff+proquestions[j]+nameListi)
      else:
        recodevars.append(promain+mathread+stratdiff+suffix[i]+proquestions[j]+nameListi)
  recodeString = " ".join(recodevars)
  recodeline = "recode "+recodeString+" (1=1) (2=1) (else = 0).\n"      
  return recodeline
  
def makeComputeLines(suffix,proquestions,promain,mathread,stratdiff,nameListi,labelListi):
  computeLines = []
  for i in range(len(suffix)):
    varString = computeVars(suffix[i], proquestions,promain,mathread,stratdiff,nameListi)
    computeLines.append("compute " + labelListi + suffix[i] + " = " + varString+".\n")
  computeBlock = "".join(computeLines)
  return computeBlock + "\n"


def computeVars(suffixi, proquestions,promain,mathread,stratdiff,nameListi):
  Vars = []
  for i in range(len(proquestions)):
    if (mathread== "r"):
      Vars.append(promain+ mathread + suffixi+ stratdiff+ proquestions[i] + nameListi)
    else:
      Vars.append(promain+ mathread + stratdiff+ suffixi+ proquestions[i] + nameListi)
  varString = " + ".join(Vars)
  return varString
  

def makeGLMtext():
  text = """
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
  return text
  
def printCompute(varlist,string,suffix,GLMtext, file):
  text = ""
  for suff in suffix:
    text = text + "compute " + string + suff + " = ("
    for i in range(len(varlist)):
      text = text + varlist[i] + suff
      if i < (len(varlist)-1):
        text = text + " + "
    text = text + ")/" + str(len(varlist)) + ".\n"
  file.write(text)
  GLMlinevars = ""
  for suff in suffix:
    GLMlinevars = GLMlinevars + string + suff + ' '
  GLMline = "GLM " + GLMlinevars + "BY sex"
  file.write(GLMline)
  file.write(GLMtext)
  file.write('\n')

