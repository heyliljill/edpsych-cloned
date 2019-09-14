# 3.a. math interest vs reading non interest on read thoroughly/skim/topic

"""SORT CASES BY mathspint. 
SPLIT FILE SEPARATE BY mathspint.
FREQUENCIES variables = m3how
/ORDER=ANALYSIS. 
SPLIT FILE OFF."""

# b. what was easy hard (math interest vs math non interest)

"""FREQUENCIES variables = m3nease m3ixease m3iyease m3izease m3bxease m3byease m3bzease
/ORDER=ANALYSIS."""

"""SORT CASES BY mathspint. 
SPLIT FILE SEPARATE BY mathspint.
FREQUENCIES variables =  m3nease m3ixease m3iyease m3izease m3bxease m3byease m3bzease
/ORDER=ANALYSIS. 
SPLIT FILE OFF."""


# c. rank order


nameList = ['num', 'nsz', 'nnof', 'cio', 'dec', 'chop', 'step', 'len', 'word', 'key', 'info', 'ano', 'vis', 'ket', 'kec', 'lket', 'lkec','pat', 'pac', 'nat', 'nac', 'proc','mexp']
labelList = ['numbers', 'sizenumbers', 'numnumbers','compoperation', 'decoding', 'choseoperation','numsteps','length','wording','keywords','extramissinfo','allnums','visualization','topicknowexp','contentknowexp','lacktopicknowexp','lackcontentknowexp', 'posaffecttopic','posaffectcontent','negaffecttopic','negaffectcontent','process','mathexp']
prefix = ['m3n','m3ix','m3iy','m3iz','m3bx','m3by','m3bz']

reasonslist = ""
for i in range(len(prefix)):
  for j in range(len(nameList)):
    reason = prefix[i]+nameList[j]
    reasonslist = reasonslist + " " + reason

text = """FREQUENCIES VARIABLES=""" + reasonslist + """
      /ORDER=ANALYSIS.""" 

# d. rank order broken by thoroughly/skim/topic


file = open('InterviewMQ3.txt','w+')

"""SORT CASES BY m3how. 
SPLIT FILE SEPARATE BY m3how."""

text
file.write(text)

"""
SPLIT FILE OFF."""
