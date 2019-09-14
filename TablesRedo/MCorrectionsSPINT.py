# 5.(Table 7) mean number of corrections, by type, out of 12 problems
# a. another step (pmim1ano), computational (pmim1com), copying (pmim1cop), operation/key (pmim1opk), operations choice (pmim1opc)
# b. Break up into interest, difficulty, gender

# pmimano = pmim1ano + pmim2ano + pmim3ano 
# pmiiano = pmii1ano + pmii2ano + pmii3ano
# pmbmano = pmbm1ano + pmbm2ano + pmbm3ano
# pmbiano = pmbi1ano + pmbi2ano + pmbi3ano 

# pmimcom = pmim1com + pmim2com + pmim3com 
# pmiicom = pmii1com + pmii2com + pmii3com
# pmbmcom = pmbm1com + pmbm2com + pmbm3com
# pmbicom = pmbi1com + pmbi2com + pmbi3com 

# pmimcop = pmim1cop + pmim2cop + pmim3cop 
# pmiicop = pmii1cop + pmii2cop + pmii3cop
# pmbmcop = pmbm1cop + pmbm2cop + pmbm3cop
# pmbicop = pmbi1cop + pmbi2cop + pmbi3cop 

# pmimopk = pmim1opk + pmim2opk + pmim3opk 
# pmiiopk = pmii1opk + pmii2opk + pmii3opk
# pmbmopk = pmbm1opk + pmbm2opk + pmbm3opk
# pmbiopk = pmbi1opk + pmbi2opk + pmbi3opk 

# pmimopc = pmim1opc + pmim2opc + pmim3opc 
# pmiiopc = pmii1opc + pmii2opc + pmii3opc
# pmbmopc = pmbm1opc + pmbm2opc + pmbm3opc
# pmbiopc = pmbi1opc + pmbi2opc + pmbi3opc 


f = open('manova-correctionsSPINT','w+')

def main():

  mathread = "m"
  
  for i in range(0,2):
    ## SELECT HIGH INTEREST ## 
    filtersign = ["~=","="]
    if mathread == "m":
      spint = "mathspint"
    elif mathread == "r":
      spint = "readspint"
    
    filterText = """USE ALL. \nCOMPUTE filter_$=("""+spint+filtersign[i]+ "2"+"""). \nVARIABLE LABELS filter_$ '""" + spint+filtersign[i]+ "2" +"""(FILTER)'. \nVALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'. \nFORMATS filter_$ (f1.0). \nFILTER BY filter_$. \nEXECUTE.\n\n"""
  
    f.write(filterText)
    
    compute = """COMPUTE pmimano = pmim1ano + pmim2ano + pmim3ano. 
VARIABLE LABELS  pmimano '# of another step corrections in all problems in interest mastery level math'. 
EXECUTE.
COMPUTE pmiiano = pmii1ano + pmii2ano + pmii3ano. 
VARIABLE LABELS  pmiiano '# of another step corrections in all problems in interest instructional level math'. 
EXECUTE.
COMPUTE pmbmano = pmbm1ano + pmbm2ano + pmbm3ano. 
VARIABLE LABELS  pmbmano '# of another step corrections in all problems in boring mastery level math'. 
EXECUTE.
COMPUTE pmbiano = pmbi1ano + pmbi2ano + pmbi3ano . 
VARIABLE LABELS  pmbiano '# of another step corrections in all problems in boring instructional level math'. 
EXECUTE.

COMPUTE pmimcom = pmim1com + pmim2com + pmim3com. 
VARIABLE LABELS  pmimcom '# of computational corrections in all problems in interest mastery level math'. 
EXECUTE.
COMPUTE pmiicom = pmii1com + pmii2com + pmii3com. 
VARIABLE LABELS  pmiicom '# of computational corrections in all problems in interest instructional level math'. 
EXECUTE.
COMPUTE pmbmcom = pmbm1com + pmbm2com + pmbm3com. 
VARIABLE LABELS  pmbmcom '# of computational corrections in all problems in boring mastery level math'. 
EXECUTE.
COMPUTE pmbicom = pmbi1com + pmbi2com + pmbi3com . 
VARIABLE LABELS  pmbicom '# of computational corrections in all problems in boring instructional level math'. 
EXECUTE.

COMPUTE pmimcop = pmim1cop + pmim2cop + pmim3cop. 
VARIABLE LABELS  pmimcop '# of copying corrections in all problems in interest mastery level math'. 
EXECUTE.
COMPUTE pmiicop = pmii1cop + pmii2cop + pmii3cop. 
VARIABLE LABELS  pmiicop '# of copying corrections in all problems in interest instructional level math'. 
EXECUTE.
COMPUTE pmbmcop = pmbm1cop + pmbm2cop + pmbm3cop. 
VARIABLE LABELS  pmbmcop '# of copying corrections in all problems in boring mastery level math'. 
EXECUTE.
COMPUTE pmbicop = pmbi1cop + pmbi2cop + pmbi3cop . 
VARIABLE LABELS  pmbicop '# of copying corrections in all problems in boring instructional level math'. 
EXECUTE.

COMPUTE pmimopk = pmim1opk + pmim2opk + pmim3opk. 
VARIABLE LABELS  pmimopk '# of operation/key corrections in all problems in interest mastery level math'. 
EXECUTE.
COMPUTE pmiiopk = pmii1opk + pmii2opk + pmii3opk. 
VARIABLE LABELS  pmiiopk '# of operation/key corrections in all problems in interest instructional level math'. 
EXECUTE.
COMPUTE pmbmopk = pmbm1opk + pmbm2opk + pmbm3opk. 
VARIABLE LABELS  pmbmopk '# of operation/key corrections in all problems in boring mastery level math'. 
EXECUTE.
COMPUTE pmbiopk = pmbi1opk + pmbi2opk + pmbi3opk . 
VARIABLE LABELS  pmbiopk '# of operation/key corrections in all problems in boring instructional level math'. 
EXECUTE.

COMPUTE pmimopc = pmim1opc + pmim2opc + pmim3opc. 
VARIABLE LABELS  pmimopc '# of operation choice corrections in all problems in interest mastery level math'. 
EXECUTE.
COMPUTE pmiiopc = pmii1opc + pmii2opc + pmii3opc. 
VARIABLE LABELS  pmiiopc '# of operation choice corrections in all problems in interest instructional level math'. 
EXECUTE.
COMPUTE pmbmopc = pmbm1opc + pmbm2opc + pmbm3opc. 
VARIABLE LABELS  pmbmopc '# of operation choice corrections in all problems in boring mastery level math'. 
EXECUTE.
COMPUTE pmbiopc = pmbi1opc + pmbi2opc + pmbi3opc . 
VARIABLE LABELS  pmbiopc '# of operation choice corrections in all problems in boring instructional level math'. 
EXECUTE.

"""

    f.write(compute)
    f.write("""
  DATASET COPY  mainCopy1 WINDOW=FRONT.\nDATASET ACTIVATE mainCopy1.\n
  
GLM pmimano pmiiano pmbmano pmbiano BY sex
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
  
  
  GLM pmimcom pmiicom pmbmcom pmbicom BY sex
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
  
  
  GLM pmimcop pmiicop pmbmcop pmbicop BY sex
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
  
  
  GLM pmimopk pmiiopk pmbmopk pmbiopk BY sex
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
  
  GLM pmimopc pmiiopc pmbmopc pmbiopc BY sex
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


main()