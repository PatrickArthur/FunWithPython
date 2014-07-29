name = raw_input("What is your name? ")

while name != "Patrick":
  print("{} Nice to meet you, how do you like python".format(name, name))
  print "Your name length: {0}".format(len(name))
  raw_input("Press <ENTER> to exit\n")
  name = raw_input("What is your name? ")
else:
  print("{} Is my name, and I like python".format(name))
  print "Your name length: {0}".format(len(name))

