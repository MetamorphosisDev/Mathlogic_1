from fractions import Fraction
#Import module

while True :
    data = input("Masukan Hitungan :")
    olah = eval(data)
    print(data, "= ", olah)

    fraksi = Fraction(olah)
    pecahan = fraksi.limit_denominator()
    print(data, " = ", pecahan)
    print("\n")
#input in terminal(vscode): "10+10" or "10*10" or "10-10" or "10/10"
#output: "20" , "100" , "0" , "1"





