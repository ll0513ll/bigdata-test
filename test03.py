import random


s1 = set([])

esc = True

while esc:

    no = random.randrange(1,46)
    s1.add(no)

    if len(s1) == 6:

        print(s1)
        esc = False