{"filter":false,"title":"manovaSPINTmathstrat.py","tooltip":"/StratDiffManovas/manovaSPINTmathstrat.py","undoManager":{"mark":37,"position":37,"stack":[[{"group":"doc","deltas":[{"action":"removeLines","range":{"start":{"row":99,"column":0},"end":{"row":170,"column":0}},"nl":"\n","lines":["################################################################################","  ","def makeRecodeLine(suffix,proquestions,promain,mathread,stratdiff,nameListi):","  recodevars = \"\"","  if (mathread==\"r\"):","    for i in range(len(proquestions)):","        recodevars = recodevars+promain+mathread+suffix[i]+stratdiff+proquestions[i]+nameListi+\" \"","    recodeline = \"recode \"+recodevars+\"(1=1) (2=1) (else = 0).\\n\"","  else:","    for i in range(len(proquestions)):","        recodevars = recodevars+promain+mathread+stratdiff+suffix[i]+proquestions[i]+nameListi+\" \"","    recodeline = \"recode \"+recodevars+\"(1=1) (2=1) (else = 0).\\n\"      ","  return recodeline","  ","def makeComputeLines(suffix,proquestions,promain,mathread,stratdiff,nameListi,labelListi):","  computeLines = \"\"","  for i in range(len(suffix)):","    Vars = computeVars(suffix[i], proquestions,promain,mathread,stratdiff,nameListi)","    computeLines = computeLines + \"compute \" + labelListi + suffix[i] + \"=\" + Vars + \".\\n\"","  return computeLines","","  ","def computeVars(suffixi , proquestions,promain,mathread,stratdiff,nameListi):","  Vars = []","  if (mathread== \"r\"):","    for i in range(len(proquestions)):","      Vars.append(promain+ mathread + suffixi+ stratdiff+ proquestions[i] + nameListi)","    variables = \" + \".join(Vars)","    ","  else:","    for i in range(len(proquestions)):","      Vars.append(promain+ mathread + stratdiff+ suffixi+ proquestions[i] + nameListi)","    variables = \" + \".join(Vars)","  return variables","  ","def makeGLMtext():","  text = \"\"\"","  /WSFACTOR=interest 2 Polynomial diff 2 Polynomial ","  /METHOD=SSTYPE(3) ","  /EMMEANS=TABLES(sex) COMPARE ADJ(LSD) ","  /EMMEANS=TABLES(interest) COMPARE ADJ(LSD) ","  /EMMEANS=TABLES(diff) COMPARE ADJ(LSD) ","  /EMMEANS=TABLES(sex*interest) ","  /EMMEANS=TABLES(sex*diff) ","  /EMMEANS=TABLES(interest*diff) ","  /EMMEANS=TABLES(sex*interest*diff) ","  /CRITERIA=ALPHA(.05) ","  /WSDESIGN=interest diff interest*diff ","  /DESIGN=sex.","  \"\"\"","  return text","  ","def printCompute(varlist,string,suffix,GLMtext, file):","  text = \"\"","  for suff in suffix:","    text = text + \"compute \" + string + suff + \" = (\"","    for i in range(len(varlist)):","      text = text + varlist[i] + suff","      if i < (len(varlist)-1):","        text = text + \" + \"","    text = text + \")/\" + str(len(varlist)) + \".\\n\"","  file.write(text)","  GLMlinevars = \"\"","  for suff in suffix:","    GLMlinevars = GLMlinevars + string + suff + ' '","  GLMline = \"GLM \" + GLMlinevars + \"BY sex\"","  file.write(GLMline)","  file.write(GLMtext)","  file.write('\\n')","  ",""]}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":0},"end":{"row":1,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":0},"end":{"row":1,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":0},"end":{"row":0,"column":13}},"text":"GLMfunctions."}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":12},"end":{"row":0,"column":13}},"text":"."}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":11},"end":{"row":0,"column":12}},"text":"s"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":10},"end":{"row":0,"column":11}},"text":"n"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":9},"end":{"row":0,"column":10}},"text":"o"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":8},"end":{"row":0,"column":9}},"text":"i"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":7},"end":{"row":0,"column":8}},"text":"t"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":6},"end":{"row":0,"column":7}},"text":"c"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":5},"end":{"row":0,"column":6}},"text":"n"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":4},"end":{"row":0,"column":5}},"text":"u"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":3},"end":{"row":0,"column":4}},"text":"f"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":2},"end":{"row":0,"column":3}},"text":"M"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":1},"end":{"row":0,"column":2}},"text":"L"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":0},"end":{"row":0,"column":1}},"text":"G"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":0},"end":{"row":0,"column":1}},"text":"i"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":1},"end":{"row":0,"column":2}},"text":"m"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":1},"end":{"row":0,"column":2}},"text":"m"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":1},"end":{"row":0,"column":2}},"text":"m"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":2},"end":{"row":0,"column":3}},"text":"o"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":3},"end":{"row":0,"column":4}},"text":"p"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":3},"end":{"row":0,"column":4}},"text":"p"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":2},"end":{"row":0,"column":3}},"text":"o"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":2},"end":{"row":0,"column":3}},"text":"p"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":3},"end":{"row":0,"column":4}},"text":"o"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":4},"end":{"row":0,"column":5}},"text":"r"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":5},"end":{"row":0,"column":6}},"text":"t"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":6},"end":{"row":0,"column":7}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":7},"end":{"row":0,"column":20}},"text":"GLMfunctions."}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":19},"end":{"row":0,"column":20}},"text":"."}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":17,"column":12},"end":{"row":17,"column":25}},"text":"GLMfunctions."}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":37,"column":19},"end":{"row":37,"column":32}},"text":"GLMfunctions."}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":38,"column":21},"end":{"row":38,"column":34}},"text":"GLMfunctions."}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":57,"column":4},"end":{"row":57,"column":17}},"text":"GLMfunctions."}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":58,"column":4},"end":{"row":58,"column":17}},"text":"GLMfunctions."}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":59,"column":4},"end":{"row":59,"column":17}},"text":"GLMfunctions."}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":59,"column":17},"end":{"row":59,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1406737355973,"hash":"d06fb9b55971b187c49ca37ae1eb598deffccb8e"}