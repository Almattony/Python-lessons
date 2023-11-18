

mahsulotlar = ['sabiz', 'qiyar', 'banan', "o'rik", 'kapusta', 'alcha', 'qulpinay', 'pomidor', 'qawin', 'qarbiz']
savat = []
bor_mahsulot = []
mavjud_emas = []


for son in range(5):
    savat.append(input(f"{son+1} ta mahsulot kirting: "))


for mahsulot in savat:
    
    if mahsulot in mahsulotlar:
        bor_mahsulot.append(mahsulot)
    elif mahsulot not in mahsulotlar:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Quydagi mahsulotlar yoq")
    for mahsulot in mavjud_emas:
        print(mahsulot)
        print('\n')
else:
    print("siz soragan hamma mahsulotlar dukonimizda bor!")
    
    


