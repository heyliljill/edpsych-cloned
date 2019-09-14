{"filter":false,"title":"manovaMWmathdiff.py","tooltip":"/StratDiffManovas/manovaMWmathdiff.py","undoManager":{"mark":19,"position":19,"stack":[[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":118,"column":0},"end":{"row":118,"column":13}},"text":"  return Vars"},{"action":"removeLines","range":{"start":{"row":106,"column":0},"end":{"row":118,"column":0}},"nl":"\n","lines":["def computeVars(suffixi , proquestions,promain,mathread,stratdiff,nameListi):","  Vars = \"\"","  if (mathread== \"r\"):","    for i in range(len(proquestions)):","      Vars = Vars  + \" \" +promain+ mathread + suffixi+ stratdiff+ proquestions[i] + nameListi","      if (i!=len(proquestions)-1):","        Vars = Vars + \" +\"","  else:","    for i in range(len(proquestions)):","      Vars = Vars  + \" \" +promain+ mathread + suffixi+ proquestions[i] + stratdiff + nameListi","      if (i!=len(proquestions)-1):","        Vars = Vars + \" +\""]},{"action":"insertText","range":{"start":{"row":106,"column":0},"end":{"row":106,"column":77}},"text":"def computeVars(suffixi , proquestions,promain,mathread,stratdiff,nameListi):"},{"action":"insertText","range":{"start":{"row":106,"column":77},"end":{"row":107,"column":0}},"text":"\n"},{"action":"insertLines","range":{"start":{"row":107,"column":0},"end":{"row":117,"column":0}},"lines":["  Vars = []","  if (mathread== \"r\"):","    for i in range(len(proquestions)):","      Vars.append(promain+ mathread + suffixi+ stratdiff+ proquestions[i] + nameListi)","    variables = \" + \".join(Vars)","    ","  else:","    for i in range(len(proquestions)):","      Vars.append(promain+ mathread + stratdiff+ suffixi+ proquestions[i] + nameListi)","    variables = \" + \".join(Vars)"]},{"action":"insertText","range":{"start":{"row":117,"column":0},"end":{"row":117,"column":18}},"text":"  return variables"}]}],[{"group":"doc","deltas":[{"action":"removeLines","range":{"start":{"row":84,"column":0},"end":{"row":156,"column":0}},"nl":"\n","lines":["","","def makeRecodeLine(suffix,proquestions,promain,mathread,stratdiff,nameListi):","  recodevars = \"\"","  if (mathread==\"r\"):","    for i in range(len(proquestions)):","        recodevars = recodevars+promain+mathread+suffix[i]+stratdiff+proquestions[i]+nameListi+\" \"","    recodeline = \"recode \"+recodevars+\"(1=1) (2=1) (else = 0).\\n\"","  else:","    for i in range(len(proquestions)):","        recodevars = recodevars+promain+mathread+suffix[i]+proquestions[i]+stratdiff+nameListi+\" \"","    recodeline = \"recode \"+recodevars+\"(1=1) (2=1) (else = 0).\\n\"      ","  return recodeline","  ","def makeComputeLines(suffix,proquestions,promain,mathread,stratdiff,nameListi,labelListi):","  computeLines = \"\"","  for i in range(len(suffix)):","    Vars = computeVars(suffix[i], proquestions,promain,mathread,stratdiff,nameListi)","    computeLines = computeLines + \"compute \" + labelListi + suffix[i] + \"=\" + Vars + \".\\n\"","  return computeLines","","  ","def computeVars(suffixi , proquestions,promain,mathread,stratdiff,nameListi):","  Vars = []","  if (mathread== \"r\"):","    for i in range(len(proquestions)):","      Vars.append(promain+ mathread + suffixi+ stratdiff+ proquestions[i] + nameListi)","    variables = \" + \".join(Vars)","    ","  else:","    for i in range(len(proquestions)):","      Vars.append(promain+ mathread + stratdiff+ suffixi+ proquestions[i] + nameListi)","    variables = \" + \".join(Vars)","  return variables","  ","def makeGLMtext():","  text = \"\"\"","  /WSFACTOR=interest 2 Polynomial diff 2 Polynomial ","  /METHOD=SSTYPE(3) ","  /EMMEANS=TABLES(sex) COMPARE ADJ(LSD) ","  /EMMEANS=TABLES(interest) COMPARE ADJ(LSD) ","  /EMMEANS=TABLES(diff) COMPARE ADJ(LSD) ","  /EMMEANS=TABLES(sex*interest) ","  /EMMEANS=TABLES(sex*diff) ","  /EMMEANS=TABLES(interest*diff) ","  /EMMEANS=TABLES(sex*interest*diff) ","  /CRITERIA=ALPHA(.05) ","  /WSDESIGN=interest diff interest*diff ","  /DESIGN=sex.","  \"\"\"","  return text","  ","def printCompute(varlist,string,suffix,GLMtext, file):","  text = \"\"","  for suff in suffix:","    text = text + \"compute \" + string + suff + \" = (\"","    for i in range(len(varlist)):","      text = text + varlist[i] + suff","      if i < (len(varlist)-1):","        text = text + \" + \"","    text = text + \")/\" + str(len(varlist)) + \".\\n\"","  file.write(text)","  GLMlinevars = \"\"","  for suff in suffix:","    GLMlinevars = GLMlinevars + string + suff + ' '","  GLMline = \"GLM \" + GLMlinevars + \"BY sex\"","  file.write(GLMline)","  file.write(GLMtext)","  file.write('\\n')",""," ",""]}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":0},"end":{"row":1,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":1,"column":0},"end":{"row":2,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":0},"end":{"row":0,"column":1}},"text":"i"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":1},"end":{"row":0,"column":2}},"text":"m"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":2},"end":{"row":0,"column":3}},"text":"p"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":3},"end":{"row":0,"column":4}},"text":"o"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":4},"end":{"row":0,"column":5}},"text":"r"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":5},"end":{"row":0,"column":6}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":5},"end":{"row":0,"column":6}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":5},"end":{"row":0,"column":6}},"text":"t"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":6},"end":{"row":0,"column":7}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":0,"column":7},"end":{"row":0,"column":20}},"text":"GLMfunctions."}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":0,"column":19},"end":{"row":0,"column":20}},"text":"."}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":18,"column":12},"end":{"row":18,"column":25}},"text":"GLMfunctions."}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":26,"column":17},"end":{"row":26,"column":30}},"text":"GLMfunctions."}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":27,"column":19},"end":{"row":27,"column":32}},"text":"GLMfunctions."}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":44,"column":2},"end":{"row":44,"column":15}},"text":"GLMfunctions."}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":45,"column":2},"end":{"row":45,"column":15}},"text":"GLMfunctions."}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":30},"end":{"row":11,"column":30},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1406737171689,"hash":"302e9390b478beddf2b2f0288f5e6bc5248b2c61"}