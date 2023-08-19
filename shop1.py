
products=[]
def read_data():
    f=open("shop1.txt","r")
    for i in f :
        mahsol=i.split(",")
        dic={"id":mahsol[0],"name":mahsol[1],"price":mahsol[2],"count":mahsol[3]}
        products.append(dic)       
def show_menu():
    print("1_show products")
    print("2_add")
    print("3_delete")
    print("4_search")
    print("5_buy")
    print("6_edit")
    print("7_exit")
    


def add():
    id=input("Enter id's kala :")
    name=input("Enter name's kala: ")
    price=input("Enter price for kala: ")
    count=input("Enter count of kala: ")
    dic={"id":id,"name":name,"price":price,"count":count}
    products.append(dic)
    print(products)
    print("add shod")








def delete():
    id=input("Enter id's kala:  ")
    for mahdol in products:
        if id==mahdol["id"]:
            products.remove(mahdol)
            print(products)
            print(mahdol,"hazf shod!!!!!!!")
            break
        else:
            print("kala ba in id iaft nzshod!!!!!!")
            break



def search():
    show_menu()
    key=input("Enter your key : ")
    for mahsol in products:
        if key==mahsol["id"] or key==mahsol["name"] :
            print(mahsol)
            break
    else:
        print("not found!!!")



def buy():
    list=[]
    while True:
        id=input("Enter id's kala or ( finish): ")
        if id=="finish":
            
            break
        for kala in products:

            if id==kala["id"]:
                print("in kala ba in id mojod ast")
                count=(input("Enter count ke mikhai: "))
                if int(count)<int(kala["count"]) or int(count)== int(kala["count"]):
                    print("mojod ast")
                    tedad=kala["count"]
                    kala["count"]=int(kala["count"])-int(count)
                    print(tedad,"be",kala["count"],"taghir kard!!!!!!!!!!")
                    use= {"id":kala["id"],
                        "name":kala["name"],
                        "price":kala["price"],
                        "count":count}
                    list.append(use)
                    
                    for use in list:
                        
                        print(int(use["price"])*int(use["count"]))

    gheimat=0
    for use in list:
        gheimat=(gheimat+(int(use["count"])*int(use["price"])))
    print("gheimat majmo:",gheimat)
                    
            
                
            



def edit():
    id=input("Enter id's kala: ")
    for mahsol in products:
        if id==mahsol["id"]:
            print("1_Name")
            print("2_Price")
            print("3_Count")
            user=int(input("Enter a number 1 ta 3:   "))
            if user==1:
                new_name=input("Enter a new name:   ")
                name=mahsol["name"]
                mahsol["name"]=new_name
                print("name:",new_name)
                print(name, "___________>>>" ,new_name,"taghir kard")
                break
            elif user==2:
                new_price=int(input("Enter a new price:  "))
                price=mahsol["price"]
                mahsol["price"]=new_price
                print("price:",new_price)
                print(price,"__________>>>>",new_price,"taghir kard")
                break
            elif user==3:
                new_count=int(input("Enter a new count:  "))
                count=mahsol["count"]
                mahsol["count"]=new_count
                print("count: ",new_count)
                print(count,"__________>>>>",new_count,"taghir kard")
                break
        else:
            print("not found")
            break
        


def exit():
    pass



def show_products():
    print("id \t name \t price \t count \t")
    print()
    for kala1 in products:
        print(kala1["id"],"\t",kala1["name"],"\t",kala1["price"],"\t",kala1["count"],"\t")
read_data()
show_menu()



user_Asli=int(input("Enter a number  1 ta 7 : "))
while True:
    if user_Asli==1:
        show_products()
        break
    elif user_Asli==2:
        add()
        break
    elif user_Asli==3:
        delete()
        break
    elif user_Asli==4:
        search()
        break
    elif user_Asli==5:
        buy()
        break
    elif user_Asli==6:
        edit()
        break
    elif user_Asli==7:
        exit()
        break
    else:
        print("ERORR!!!  ENTER ADAD BEIN 1 TA 7")



read_data()
show_menu()