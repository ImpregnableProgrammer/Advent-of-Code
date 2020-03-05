
def First_Part(layers, w, h):
    Mlayer = min([layers[i:i+w*h] for i in range(0, len(layers), w*h)], key = lambda h:h.count('0'))
    return Mlayer.count('1') * Mlayer.count('2')

def Second_Part(layers, w, h):
    Layers = [layers[i:i+w*h] for i in range(0, len(layers), w*h)]
    image = ""
    for i in range(w*h):
        for l in Layers:
            if l[i] in "01":
                image += l[i]
                break
    for j in range(0, w*h, w):
        print(image[j:j+w].replace('0', ' '))
                

layers, w, h = "123456789012", 3, 2
layers, w, h = "0222112222120000", 2, 2
layers, w, h = ''.join(open("Inputs/Day_08.txt", "r").read().split('\n')), 25, 6

print(First_Part(layers, w, h))
Second_Part(layers, w, h)
    
