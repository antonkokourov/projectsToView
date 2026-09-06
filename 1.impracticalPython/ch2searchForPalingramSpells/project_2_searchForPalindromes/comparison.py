

list1 = ['naan', 'tut', 'dad', 'minim', 'radar', 'dud', 'kayak', 'boob', 'stats', 'i', 'pep', 'level', 'peep', 'nan', 'sis', 'eve', 'bib', 'ewe', 'tenet', 'ere', 'rotor', 'pip', 'mum', 'aha', 'a', 'toot', 'solos', 'pop', 'pup', 'refer', 'eke', 'bub', 'gig', 'madam', 'sexes', 'pap', 'tit', 'wow', 'redder', 'poop', 'gag', 'eye', 'deified', 'tot', 'nun', 'hah', 'bob', 'did', 'civic', 'mom', 'p', 'deed', 'huh', 'tat', 'sees', 'sagas', 'mam', 'kook', 'noon']
list2 = ['aha', 'bib', 'bob', 'boob', 'bub', 'civic', 'dad', 'deed', 'deified', 'did', 'dud', 'eke', 'ere', 'eve', 'ewe', 'eye', 'gag', 'gig', 'hah', 'huh', 'kayak', 'kook', 'level', 'madam', 'mam', 'minim', 'mom', 'mum', 'naan', 'nan', 'noon', 'nun', 'pap', 'peep', 'pep', 'pip', 'poop', 'pop', 'pup', 'radar', 'redder', 'refer', 'rotor', 'sagas', 'sees', 'sexes', 'sis', 'solos', 'stats', 'tat', 'tenet', 'tit', 'toot', 'tot', 'tut', 'wow']

for w in list1:
    if w not in list2:
        print(w)

print("____________")
for w in list2:
    if w not in list1:
        print(w)