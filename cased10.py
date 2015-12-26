import sys

def case(x, k = 0):
    print(x)
    for i in range(k, len(x)):
        case(x[:i]+x[i].upper()+x[i+1:], i+1)
    return

s = sys.stdout
f =open('dict.lst', 'r')
output = open('cased10length.lst', 'w')
sys.stdout = output

for line in f:
    line = line.strip()
    if len(line) == 10: 
        s.write(line+'\n')
        case(line)

output.close()
f.close()