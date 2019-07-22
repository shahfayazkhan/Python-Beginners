one = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
        "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen",
        "Eighteen","Ninteen"]

ten = ["","Ten","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]

def convert(number):
    if number == 0:
        return "Zero"
    elif number < 20:
        return one[number]
    elif number < 100:
        return ten[int(number/10)]+" "+one[int(number%10)]
    elif number < 1000:
        return convert(int(number/100))+" Hundred "+convert(int(number%100))
    elif number < 100000:
        return convert(int(number/1000))+" Thousand "+convert(int(number%1000))
    elif number < 1000000:
        return convert(int(number/100000))+" Lac "+convert(int(number%100000))
    elif number < 10000000:
        return convert(int(number/1000000))+" Million "+convert(int(number%1000000))
    
    

user = int(input("Please Enter Value : "))

print("Converted : "+str(convert(user))+" Only")


