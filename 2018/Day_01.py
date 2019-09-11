
def First_Part(freqs):
    i = 0;
    for value in freqs:
        i += int(value)
    return i

Input = open("Inputs/Day_01.txt", "r").read().split('\n')[:-1]
print(First_Part(Input))
        
def Second_Part(freqs):
    freq_list = set()
    size = len(freqs)
    freq = i = 0
    while True:
        freq_list.add(freq)
        freq += int(freqs[i % size])
        i += 1
        if freq in freq_list:
            return freq

print(Second_Part(Input))
