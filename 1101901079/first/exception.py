import sys
randomList = ["a",0,2]
for entry in randomList:
 try:
  print("The entry is: ", entry)
  r = 1/int(entry)
  break
 except:
  print("ops!!", sys.exc_info()[0],"occured")
  print("next entry")
  print()
print("The reciprocal of",entry,"is",r)