
filepath = '/home/name404/Desktop/3.txt'
with open(filepath) as fp:
   line = fp.readline()
   count = 1
   while line:
       print("Line {}: {}".format(count, line.strip()))
       line = fp.readline()
       count += 1

