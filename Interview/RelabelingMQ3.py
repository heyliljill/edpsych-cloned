file = open('RelabelingMQ3.txt','w+')
file.write("VARIABLE LABELS\n")


levelsVar = ["i", "b"]
sublevelsVar = ["x", "y", "z"]
nameVar = ["ease", "num", "nsz", "nnof", "cio", "dec", "chop",  "step", "len",  "word", "key", "info", "ano", "vis", "ket", "kec", "lket", "lkec", "pat", "pac","nat", "nac", "proc", "mexp"]

levelsLabels= ["interesting","boring"]
sublevelsLabels = ["1", "2", "3"]
nameLabels = ["level of easiness", "numbers", "size of numbers", "number of numbers", "computation in operation", "decoding", "choosing operation", "number of steps", "length of problem", "wording", "key words", "extra", "use all numbers", "visualization", "know or exp. topic", "know or exp. content", "lack of know or exp. topic", "lack of know or exp. content", "positive affect topic", "positive affect content", "negative affect topic","negative affect content", "process", "math experience"]


for i in range(len(nameVar)):
  for j in range(len(levelsVar)):
    for k in range(len(sublevelsVar)):
      variable = "m3" + levelsVar[j] + sublevelsVar[k] + nameVar[i]
      label = "math Q3-" + levelsLabels[j] + " #" + sublevelsLabels[k] + "-" + nameLabels[i]
      command = variable +  " \'" + label + "\'"
      file.write(command)
      file.write("\n")

file.write ('.')

file.write("\n\n\n\n\n\n")
file.write("VALUE LABELS\n")


for j in range(len(levelsVar)):
  for k in range(len(sublevelsVar)):
    variable = "m3" + levelsVar[j] + sublevelsVar[k] + "ease "
    file.write(variable)
values = """
0 "no info"
1 "easiest"
2 "easy"
3 "hardest"
4 "hard"
5 "medium".
"""
file.write(values)

file.write("\n\n\n\n\n\n")
file.write("VALUE LABELS\n")


for i in range(1, len(nameVar)):
  for j in range(len(levelsVar)):
    for k in range(len(sublevelsVar)):
      variable = "m3" + levelsVar[j] + sublevelsVar[k] + nameVar[i] + " "
      file.write(variable)
values = """
0 "no"
1 "yes".
"""
file.write(values)
