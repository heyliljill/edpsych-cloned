file = open('InterviewRQ2-reasons.txt','w+')

nameList = ['read', 'rrg', 'rrcom', 'rrsf', 'sab', 'usu', 'para', 'page', 'vis', 'rits', 'sc', 'cued', 'notes', 'main', 'title', 'ke', 'dist1', 'dist2', 'dist3']
labelList = ['readfirst', 'rereadgeneral', 'rereadcomp', 'rreadfact', 'startbegin', 'setup', 'paragraph', 'picturepage', 'visualize', 'repeatsinfo', 'streamconsciousness','cued','notes', 'mainideas','title','knowledgeexp','distinguish1','distinguish2','distinguish3']

prefix = 'rtw'

reasonslist = ""
for j in range(len(nameList)):
  reason = prefix+nameList[j]
  reasonslist = reasonslist + " " + reason

text = """FREQUENCIES VARIABLES=""" + reasonslist + """
      /ORDER=ANALYSIS.""" 
  
file.write(text)
  


"""SORT CASES BY readspint. 
SPLIT FILE SEPARATE BY readspint."""


"""
SPLIT FILE OFF."""
