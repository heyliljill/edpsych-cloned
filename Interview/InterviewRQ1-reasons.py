file = open('InterviewRQ1-reasons.txt','w+')

nameList = ['voc', 'len', 'lit', 'lot', 'writ', 'struc', 'comp', 'int', 'vis', 'ket', 'kec', 'lket', 'lkec', 'pat', 'pac', 'nat', 'nac']
labelList = ['vocabulary', 'length', 'littleinfo', 'lotsinfo', 'writstyle', 'structure', 'comprehension', 'interestingboring', 'visualization', 'topicknowexp', 'contentknowexp','lacktopicknowexp','lackcontentknowexp', 'posaffecttopic','posaffectcontent','negaffecttopic','negaffectcontent']

prefix = ['rim','rii','rbm','rbi']

extra = """FREQUENCIES VARIABLES=rimease riiease rbmease rbiease 
  /ORDER=ANALYSIS."""
  
file.write(extra)

reasonslist = ""
for i in range(len(prefix)):
  for j in range(len(nameList)):
    reason = prefix[i]+nameList[j]
    reasonslist = reasonslist + " " + reason

text = """FREQUENCIES VARIABLES=""" + reasonslist + """
      /ORDER=ANALYSIS.""" 
  
file.write(text)
