s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material in this guide, then the Python Mentors group is available to help guide new contibutors through the process. """

a = s.replace('.', '')
a = a.replace(',', '')
a = a.upper().split(' ')
a.remove('')
word_result = set([])

for list in a:

    c = a.count(list)
    word_result.add(list+" : %d" %c)

rlist = []
for result in word_result:

    rlist.append(result)
    rlist.sort()

for i in rlist:

    print(i)













