constant = 6.022 * 10 ** 23
def num_atoms(grams , atomicWeight = 196.67):
    result = ((constant) / atomicWeight) * grams
    print(result)

num_atoms(10)
num_atoms(10, 12.001)
num_atoms(10, 1.008)