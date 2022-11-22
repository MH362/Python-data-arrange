Int = []
Float = []
Str = []


def add(Int ,Float, Str):
    B = input("Input: ")
    try:
        Chk = int(B)
        print(f"Input type: {type(Chk)}")
        print("=========================")
        Int.append(Chk)
        print(f"\nInt: {Int}\nFloat: {Float}\nStr: {Str}")
#        if (len(Float) != 0) :
#            print(f"Data update: \nInt: {Int}\nFloat: {Float}")
#            print("#########################")
#        elif (len(Float) != 0) and (len(Str) != 0):
#            print(f"Data update: \nInt: {Int}\nStr: {Str}\nFloat: {Float}")
#            print("#########################")
#        elif (len(Str) != 0) :
#            print(f"Data update: \nInt: {Int}\nStr: {Str}")
#            print("#########################")
        add(Int, Float, Str)
    except ValueError:
        try :
            Chk = float(B)
            print(f"Input type: {type(Chk)}")
            print("=========================")
            Float.append(Chk)
            print(f"\nInt: {Int}\nFloat: {Float}\nStr: {Str}")
#            if (len(Int) != 0) :
#               print(f"Data update: \nInt: {Int} \nFloat: {Float}")
#                print("#########################")
#            elif (len(Int) != 0) and (len(Str) != 0):
#               print(f"Data update: \nInt{Int}\nStr{Str}\nFloat{Float}")
#               print("#########################")
#           elif (len(Str) != 0) :
#               print(f"Data update: \nFloat{Float}\nStr{Str}")
#                print("#########################")
            add(Int, Float, Str)
        except ValueError:
            Chk = str(B)
            print(f"Input type: {type(Chk)}")
            print("=========================")
            Str.append(Chk)
            print(f"\nInt: {Int}\nFloat: {Float}\nStr: {Str}")
#            if (len(Int) != 0) :
#                print(f"Data update: \nInt: {Int} \nStr: {Str}")
#                print("#########################")
#            elif (len(Float) != 0) and (len(Int) != 0):
#                print(f"Data update: \nInt{Int}\nStr{Str}\nFloat{Float}")
#                print("#########################")
#            elif (len(Float) != 0) :
#                print(f"Data update: \nFloat{Float}\nStr{Str}")
#                print("#########################")
            add(Int, Float, Str)
            


add(Int, Float, Str)