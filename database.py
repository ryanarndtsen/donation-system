DELIM = ', '

def read_record(first):
    with open('db.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(first):
                frags = line.split(DELIM)
                try:
                    frags[1] = int(frags[1])
                except ValueError:
                        continue
                return frags


def write_record(name, age, password):
    with open('db.txt', 'r') as f:
        for line in f:
            line = line.strip()
            frags = line.split(DELIM)
            if (frags == [first, age, password]):
                print('record already exists')
                return
    with open('db.txt', 'a+') as f:
        f.write("{}, {}, {}".format(name, age, password))


write_record('john', 20, 'hello123')
print(read_record("john" ))
print(read_record("Frank"))
