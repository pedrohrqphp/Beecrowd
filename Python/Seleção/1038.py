opcao = input().split()

cod = int(opcao[0])
quant = int(opcao[1])

if cod == 1:
    total = 4.00 * quant
    print('Total: R$ %.2f' % total)

elif cod == 2:
    total = 4.50 * quant
    print('Total: R$ %.2f' % total)

elif cod == 3:
    total = 5.00 * quant
    print('Total: R$ %.2f' % total)

elif cod == 4:
    total = 2.00 * quant
    print('Total: R$ %.2f' % total)

elif cod == 5:
    total = 1.50 * quant
    print('Total: R$ %.2f' % total)