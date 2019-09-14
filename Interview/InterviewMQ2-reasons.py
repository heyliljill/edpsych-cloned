file = open('InterviewMQ2-reasons.txt','w+')

nameList = ['rtf', 'rrg', 'rrfc', 'rrfn', 'chop', 'docomp', 'part', 'sent', 'ucon', 'ke', 'vis', 'sketch', 'pphr', 'key', 'speech', 'est', 'uano', 'nag', 'reasop','ktchop','chg','chcomp','chreas','chasu']
labelList = ['readfirst', 'rereadgeneral', 'rereadcomp', 'rreadnumbers', 'chooseoperation', 'computation', 'isolatespart', 'sentence', 'context', 'knowexp', 'visualize','sketch','paraphrase', 'keywords','speech','estimates','usesallnum','numberguess','reasonableop','knowtochoseop','checkgeneral','checkcomp','cheackreasonable','checkaltsetup']

prefix = 'm2'

reasonslist = ""
for j in range(len(nameList)):
  reason = prefix+nameList[j]
  reasonslist = reasonslist + " " + reason

text = """FREQUENCIES VARIABLES=""" + reasonslist + """
      /HISTOGRAM 
      /ORDER=ANALYSIS.""" 
  
file.write(text)
  


"""SORT CASES BY mathspint. 
SPLIT FILE SEPARATE BY mathspint."""


"""
SPLIT FILE OFF."""
