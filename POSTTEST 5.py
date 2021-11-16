import os
import secrets as randomday

data = {
    'Food' : {'Nasi Goreng':15000, 'Mie Goreng':16000, 'Beef Burger':25000, 'Special Omelette':20000, 'Spaghetti':22000, 'Bakso':12000},
    'Drink' : {'Ice Tea':5000, 'Ice Coffee':8000, 'Milkshake':9000, 'Aqua':4000, 'Orange Juice':15000, 'Soft Drink':8000},
}

FoodCart = []
DrinkCart = []
PriceFood = []
PriceDrink = []

def Poster():
        print("""
|---------------------------------------------------| 
|              Welcome to Our Restaurant            |
| ================================================= | 
| ------------------------------------------------- | 
""")

def ClearMenu():
        os.system('cls' if os.name == 'nt' else 'clear') 

def FoodInput():
        F = 1
        print("\n==========================================")
        print("Silahkan Pesan Makanan sesuai selera anda")
        print("Ketik 'selesai' jika selesai memesan")
        print("==========================================")
        while F > 0:
                OrderF = data ['Food']
                FoodOrder = input("Silahkan Pesan Makanan anda = ")
                if FoodOrder in OrderF.keys():
                        FoodCart.append(FoodOrder)
                        PriceFood.append(data['Food'][FoodOrder])

                elif FoodOrder == 'selesai' or FoodOrder == 'Selesai':
                        DrinkMenu()
                        DrinkInput()
                        break

# Input Minuman #
def DrinkInput():
        D = 1
        print("==========================================")
        print("Silahkan Pesan Minuman sesuai selera anda")
        print("Ketik 'selesai' jika selesai memesan")
        print("==========================================")
        while D > 0:
                OrderD = data ['Drink']
                DrinkOrder = input("Silahkan Pesan Minuman anda = ")
                if DrinkOrder in OrderD.keys():
                        DrinkCart.append(DrinkOrder) 
                        PriceDrink.append(data['Drink'][DrinkOrder])
                elif DrinkOrder == 'selesai' or DrinkOrder == 'Selesai':
                        Buy()
                        break

def Buy():

        TotalFoodPrice = sum(PriceFood)
        TotalDrinkPrice = sum(PriceDrink)

        diskon = 0

# Pemilihan hari beli dilakukan secara acak #
        TotalHari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
        HariBeli = randomday.choice(TotalHari)

# Pengaplikasian Diskon Makanan Jika Beli >2 #
        if len(FoodCart) >= 2:
                print("\n================================================================")
                print("Pesanan Makanan Anda : ")
                for FL in FoodCart:
                        print(FL)
                print("Total Harga : Rp.", TotalFoodPrice)
                print("==================================================================")
                print("Anda mendapat diskon sebesar 5% karena memesan 2 menu atau lebih.")
                print("Mohon siapkan uang pas atau kembalian anda menjadi milik kami")
                print("==================================================================")
                diskon+=5

        else:
                print("==================================================================")
                print("Pesanan Makanan Anda : ")
                for FL in FoodCart:
                        print(FL)
                print("Total Harga : Rp.", TotalFoodPrice)  
                print("=========================================")  
                print("Gak diskon ya bang karena pesen 1 doang")
                print("=========================================")


# Pengaplikasian Diskon Minuman Jika Beli >3 #
        if len(data['Drink']) >= 3:
                print("===================================================================")
                print("Pesanan Minuman Anda : ")
                for DL in DrinkCart:
                        print(DL)
                print("Total Harga : Rp.", TotalDrinkPrice)
                print("===================================================================")
                print("Anda mendapat diskon sebesar 10% karena memesan 3 menu atau lebih")
                print("Mohon siapkan uang pas atau kembalian anda menjadi milik kami")
                print("===================================================================")
                diskon+=10
        else:
                print("====================================================================")
                print("Pesanan Minuman Anda : ")
                for DL in DrinkCart:
                        print(DL)
                print("Total Harga : Rp.", TotalDrinkPrice)
                print("Gak diskon ya bang karena pesen 1 doang")
                print("====================================================================")

        TotalPrice = TotalDrinkPrice + TotalFoodPrice

# Pengaplikasian Diskon Pembayaran #
        print("\n=======================================")
        print("Silahkan Pilih Metode Pembayaran : ")
        print("1. Uang Cash. \n2. Credit Card. \n3. e-wallet. \n4. Ngutang")
        print("=======================================")

        Metode = input("Saya Memilih = ")
        if Metode == 'E-Wallet' or Metode == 'e-wallet':
                print("=================================================")
                print("Hore Diskon Tambahan berhasil didapat Sebesar 5% ")
                print("=================================================")
                diskon+=5
        elif Metode == 'Ngutang' or Metode == 'ngutang':
                print("Mau dipukul apa gimana?")
                print("==========================")
        else:
                print("================================")
                print("Total Harga : Rp.", TotalPrice)
                print("Gak diskon ya bang")
                print("================================")

        # Pengaplikasian Diskon Hari #
        print("\n==========================================================")
        print("Eits, masih ada diskon tambahan. \nHari ini hari apa hayo")
        if HariBeli == 'Sabtu' or HariBeli == 'Minggu':
                print("Hore, karena hari ini hari", HariBeli, "\nKamu dapat diskon tambahan sebesar 5%")
                diskon+=5
                
        else:
                print("Hore, karena hari ini hari", HariBeli, "Kamu dapat diskon tambahan sebesar 10%")
                diskon+=10

        print("==========================================================")
        print("Total diskon kamu sebesar = "+str(diskon)+"%")
        print('=',TotalPrice,"-",(diskon/100*TotalPrice))

        TotalPrice = TotalPrice - (diskon/100*TotalPrice)
        print("Jadi total harga yang kamu bayar = Rp.", TotalPrice)
        print("==========================================================")

        print("\n=============================================================")
        print("terima kasih telah berbelanja! \nJangan lupa kembali untuk menghamburkan duit anda")
        print("==============================================================")
        ExitProgram()
        

def Main():
        ClearMenu()
        Poster()
        print("=====What You Want to Do?=====")
        print("[1] Show Food Menu")
        print("[2] Show Drink Menu")
        print("[3] Add New Menu")
        print("[4] Change Menu")
        print("[5] Delete Menu")
        print("[0] Quit Program")
        print("=" * 29)

        SelectedOption = input("Choose number> ")
        print("=" * 29)
        if(SelectedOption == "1"):
                FoodMenu()
                FoodInput()
        elif(SelectedOption == "2"):
                DrinkMenu()
                DrinkInput()
        elif(SelectedOption == "3"):
                AddMenu()
        elif(SelectedOption == "4"):
                ChangeMenu()
        elif(SelectedOption == "5"):
                DeleteMenu()
        elif(SelectedOption == "0"):
                print("\n======================")
                print("Thanks for your visit \nHave a good day")
                print("======================")
                exit()
        else:
                print("We can't identify your input.")
                Back()

def Back():
        print("\n")
        input("Tekan Enter untuk kembali...")
        Main()

def ExitProgram():
        print("=" * 30)
        print("Thanks for using our programs \nExiting program...")
        print("=" * 30)
        exit

def FoodMenu():
        print("\n============================================")
        print("                Food Menu                   ")
        print("============================================")
        num = 1
        x = data['Food']
        for food in x:
                print("{} = Rp.{}".format(food,x[food]))
                num+=1
        print('============================================')

def DrinkMenu():
        print("============================================")
        print("                Drink Menu                  ")
        print("============================================")
        num = 1
        y = data['Drink']
        for drink in y:
                print("{} = Rp.{}".format(drink,y[drink]))
                num+=1
        print('===============================')


def AddMenu():
        # Add Menu Makanan di AKhir #
        F = 1
        AddFood = input("Input your new food name = ")
        AddFPrice = input("Input the menu price = ")
        data['Food'][AddFood] = AddFPrice
        F +=1
        choose = input("Do you want to add another food? (Yes/Continue) ")
        if choose == 'Yes' or choose == 'yes':
                AddMenu()
        elif choose == 'Continue' or choose == 'continue':
                        AddDrink()
        else:
                print("=" * 30)
                print("We cant identify your input. \nPlease Try Again...")
                print("=" * 30)
                Main()

def AddDrink():
        # Add Menu Minuman di Akhir #
        D = 1
        print("\n==========================================")
        AddDmenu = input("Input your new drink name = ")
        AddDPrice = input("Input the menu price = ")
        data['Drink'][AddDmenu] = AddDPrice
        D +=1
        choose = input("Do you want to add another drink? ")
        if choose == 'Yes' or choose == 'yes':
                AddDrink()
        elif choose == 'No'or choose =='no':
                print("=\n=========================")
                print("changes saved successfully")
                print("==========================")
        Back()

def ChangeMenu():
        print("\n=============== Change Menu ================")
        choose = input("Which one do you want to edit? (Food/Drink) ")
        print("============================================")
        if choose == 'Food' or choose == 'food':
                FoodMenu()
                Foods = data["Food"]
                x = input("Choose Food That You Want to Edit : ") 
                if x in Foods.keys() :
                    new_food = input("Input your new food name = ")
                    new_fprice = int(input("Input your new food price = "))
                    Foods.pop(x)
                    Foods.update({new_food:new_fprice})

                    print("===================================")
                    print("Change has been successfully saved.")
                    input("Returning to menu...")
                    Back()
                    print("===================================")

                else :
                    print("===================================")
                    print("We dont have that kind of food. \nPlease try to input it correctly.")
                    print("===================================")

        elif choose == 'Drink' or choose == 'drink':
                DrinkMenu()
                Drinks = data ['Drink']
                y = input("Choose Drink That You Want to Edit : ")
                if y in Drinks.keys() :
                    new_drink = input("Input your new drink menu : ")
                    new_dprice = int(input("Input your new drink price : "))
                    Drinks.pop(y)
                    Drinks.update({new_drink:new_dprice})

                    print("===================================")
                    print("Change has been successfully saved.")
                    input("Returning to menu...")
                    Back()
                    print("===================================")

                else :
                    print("===================================")
                    print("We dont have that kind of drink. \nPlease try to input it correctly.")
                    print("===================================")
        else:
                ChangeMenu()


def DeleteMenu():
        print("\n==========================================")
        choose = input("Which one do you want to delete? (Food/Drink) ")
        print("==========================================")
        if choose == 'Food' or choose == 'food':
                FoodMenu()
                df = input("Please choose food that you want to delete = ")
                delete_food = df.title()
                if delete_food in data['Food']:
                        delete_menu = input("Do you want to delete this menu? (Yes/No) ")
                        if delete_menu == 'Yes' or delete_menu == 'yes':
                                data['Food'].pop(delete_food)
                                input("Menu has been deleted.")
                                Back()

        elif choose == 'Drink' or choose == 'drink':
                DrinkMenu()
                dd = input("Please choose drink that you want to delete = ")
                delete_drink = dd.title()
                if delete_drink in data['Drink']:
                        delete_menu = input("Do you want to delete this menu? (Yes/No) ")
                        if delete_menu == 'Yes' or delete_menu == 'yes':
                                data['Drink'].pop(delete_drink)
                                input("Menu has been deleted.")
                                Back()
                
        else:
                print("We cant identify your input. \nPlease try again ")
                DeleteMenu()
Main()