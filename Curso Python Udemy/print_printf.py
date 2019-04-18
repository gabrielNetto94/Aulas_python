
a = "Gabriel"
b = 25
c = True
d = 6.1243

print(f'{"Olá gabriel",a," sua idade é ",b," status (V ou F):",c," média ",d} ')


import sys
def printf(format, *args):sys.stdout.write(format % args)

a = "gabriel"
i = 7
pi = 3.14159265359

#printf like a C
printf("hi %s r u okay? %d %.2f\n",a, i, pi)
