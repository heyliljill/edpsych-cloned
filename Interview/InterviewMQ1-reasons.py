file = open('InterviewMQ1-reasons.txt','w+')

nameList = ['num', 'nsz', 'nnof', 'cio', 'dec', 'chop', 'step', 'len', 'word', 'key', 'info', 'ano', 'vis', 'ket', 'kec', 'lket', 'lkec','pat', 'pac', 'nat', 'nac', 'proc','mexp']
labelList = ['numbers', 'sizenumbers', 'numnumbers','compoperation', 'decoding', 'choseoperation','numsteps','length','wording','keywords','extramissinfo','allnums','visualization','topicknowexp','contentknowexp','lacktopicknowexp','lackcontentknowexp', 'posaffecttopic','posaffectcontent','negaffecttopic','negaffectcontent','process','mathexp']

prefix = ['mima','mimb','mimc','miia','miib','miic','mbma','mbmb','mbmc','mbia','mbib','mbic']

easeVars = ""
for i in range(len(prefix)):
  easeVars = easeVars + " " + prefix[i]+"ease"

  extra = """FREQUENCIES VARIABLES=""" + easeVars +"""
    /ORDER=ANALYSIS."""
    
file.write(extra)
file.write("\n\n")

reasonslist = ""
for i in range(len(prefix)):
  for j in range(len(nameList)):
    reason = prefix[i]+nameList[j]
    reasonslist = reasonslist + " " + reason
text = """FREQUENCIES VARIABLES=""" + reasonslist + """
  /ORDER=ANALYSIS.""" 
  
file.write(text)





# for j in range(len(nameList)):
#   reasonslist = ""
#   for i in range(len(prefix)):
#     reasons = prefix[i]+nameList[j]
#     reasonslist = reasonslist + reasons + " "
#   reason = labelList[j]
#   label = "m"+labelList[j]+"easy"
  

#   text = """
# COUNT """ + label + "=" + reasonslist + "(1)" + reasonslist + """(2). 
# VARIABLE LABELS """ +  label + " 'reading " + reason + """ reason - easy'. 
# EXECUTE. 
# FREQUENCIES VARIABLES=""" + label + """ 
#   /STATISTICS=STDDEV MEAN SUM 
#   /ORDER=ANALYSIS.
#   """
  
#   file.write(text)
  
# for j in range(len(nameList)):
#   reasonslist = ""
#   for i in range(len(prefix)):
#     reasons = prefix[i]+nameList[j]
#     reasonslist = reasonslist + reasons + " "
#   reason = labelList[j]
#   label = "h"+labelList[j]+"hard"
  

#   text = """
# COUNT """ + label + "=" + reasonslist + "(4)" + reasonslist + """(5). 
# VARIABLE LABELS """ +  label + " 'reading " + reason + """ reason - hard'. 
# EXECUTE. 
# FREQUENCIES VARIABLES=""" + label + """ 
#   /STATISTICS=STDDEV MEAN SUM 
#   /ORDER=ANALYSIS.
#   """
  
#   file.write(text)
  