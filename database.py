DELIM = ', '

def read_record(first):
    with open('db.txt', 'r') as f:
        for line in f:
            if line.strip().split(DELIM)[0] == first:
                frags = line.split(DELIM)
                try:
                    frags[1] = int(frags[1])
                except ValueError:
                        continue
                return frags


def write_record(name, age, password, numb, numb2, type):
    with open('db.txt', 'r') as f:
        for line in f:
            line = line.strip()
            frags = line.split(DELIM)
            if (frags[0] == name):
                print('Name already exists.')
                return
    with open('db.txt', 'a+') as f:
        f.write("{}, {}, {}, {}, {}, {}\n".format(name, age, password, numb, numb2, type))
        


'''write_record('john', 20, 'hello123', 0, 0, "Giver")
print(read_record("john" ))
print(read_record("Frank"))'''
