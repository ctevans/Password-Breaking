import sys

def leet(x, index = 0, k=0):
    if k < 2:
        for i in range(index, len(x)):
            if x[i] in leets:
                leet(x[:i]+leets[x[i]]+x[i+1:], i+1, k+1)
                
    elif k == 2:
        print(x)
    return

leets = {'L':'1', 'I':'1', 'R':'2', 'Z':'2', 'E':'3', 'A':'4', 'S':'5', 'b':'6', 'G':'6', 'T':'7', 'L':'7', 'B':'8', 'g':'9', 'q':'9', 'O':'0'}

s = sys.stdout
f =open('cased10length.lst', 'r')
output = open('leeted10length.lst', 'w')
sys.stdout = output

for line in f:
    s.write(line)
    line = line.strip()
    leet(line)

output.close()
f.close()