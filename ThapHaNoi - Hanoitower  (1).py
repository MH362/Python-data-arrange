SD = 3#int(input("Số đĩa: "))
C1 = "A"#str(input("Cột gốc: "))
C2 = "B"#str(input("Cột trung gian: "))
C3 = "C"#str(input("Cột đích: "))


def Giai(SD,C1,C2,C3):
    if SD > 0:
        #print(f"Đ1 : {C1} -> {C3}")
        #return
        Giai((SD-1), C1, C2, C3)
        print(f"CĐ{SD} : {C1} -> {C3}")
        Giai((SD-1), C1, C2, C3)




print(Giai(SD, C1, C2, C3))
