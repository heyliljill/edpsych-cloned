# 3.a. reading interest vs reading non interest on read thoroughly/skim/topic

"""SORT CASES BY readspint. 
SPLIT FILE SEPARATE BY readspint.
FREQUENCIES variables = r3how
/ORDER=ANALYSIS. 
SPLIT FILE OFF."""

# b. what was easy hard (reading interest vs reading non interest)

"""FREQUENCIES variables = r3iiease  r3biease
/ORDER=ANALYSIS."""

"""SORT CASES BY readspint. 
SPLIT FILE SEPARATE BY readspint.
FREQUENCIES variables =  r3iiease  r3biease
/ORDER=ANALYSIS. 
SPLIT FILE OFF."""


# c. rank order


nameList = ['voc', 'len', 'lit', 'lot', 'writ', 'stru', 'comp', 'int', 'vis', 'ket', 'kec', 'lket', 'lkec', 'pat', 'pac', 'nat', 'nac']
labelList = ['vocabulary', 'length', 'littleinfo', 'lotsinfo', 'writstyle', 'structure', 'comprehension', 'interestingboring', 'visualization', 'topicknowexp', 'contentknowexp','lacktopicknowexp','lackcontentknowexp', 'posaffecttopic','posaffectcontent','negaffecttopic','negaffectcontent']

prefix = ['r3ii','r3bi']

reasonslist = ""
for i in range(len(prefix)):
  for j in range(len(nameList)):
    reason = prefix[i]+nameList[j]
    reasonslist = reasonslist + " " + reason

text = """FREQUENCIES VARIABLES=""" + reasonslist + """
      /ORDER=ANALYSIS.""" 


"""DESCRIPTIVES VARIABLES=r3iiease r3iivoc r3iilen r3iilit r3iilot r3iiwrit r3iistru r3iicomp r3iiint r3iivis r3iiket r3iikec r3iilket r3iilkec r3iipat r3iipac r3iinat r3iinac r3biease r3bivoc r3bilen r3bilit r3bilot r3biwrit r3bistru r3bicomp r3biint r3bivis r3biket r3bikec r3bilket r3bilkec r3bipat r3bipac r3binat r3binac 
  /STATISTICS=MEAN SUM STDDEV MIN MAX."""


# d. rank order broken by thoroughly/skim/topic

"""SORT CASES BY r3how. 
SPLIT FILE SEPARATE BY r3how."""

text
print text

"""
SPLIT FILE OFF."""
