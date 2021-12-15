import alprogramok as p

a = int(input('add meg a hatvany alapot: '))
k = int(input('add meg a hatvany kitevot: '))

e = p.hatvanyozas(a, k)

print(f'{a}^{k} = {e}')
p.kilepes()

eredmeny = p.osszeadas('kutya', 'ól')
print(eredmeny)


lista = p.randomlista(10, 1, 30)
print(lista)