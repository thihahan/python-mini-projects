import math

from pendulum import local
local_value = 0
class Utilization_of_GDP:
    def __init__(self, one_value, two, three, five, six):
        self.one_value = one_value
        self.one_persentage = 100
        self.two = two
        self.three = three
        self.four_persentage = 0
        self.five = five
        self.six = six
    
    def main(self):
            global local_value
            first_word = 'တစ် မျိုး သား လုံး ၏ ပြည် တွင်း အ သား တင် ထုတ် လုပ် မှု နှင့် ဝန် ဆောင် မှု တန် ဖိုး'
            # first_word = first.decode('utf-8')
            two_persentage = round((self.two / self.one_value)*100, 2)
            three_persentage = round((self.three / self.one_value)*100, 2)
            four = round((self.one_value + self.two - self.three),2)
            four_persentage = round((four / self.one_value)*100, 2)
            five_persentage = round((self.five/ four * four_persentage), 2)
            six_persentage = round((self.six / four * four_persentage), 2)
            seven = round((four - (self.five + self.six)), 2)
            seven_persentage = round(((seven/four)* four_persentage),2)
            seven_persentage = round((seven / four * four_persentage), 2)
            print(f"                 အ ကြော င်း အ ရာ                                        ကျပ် သန်း ပေါင်း       ရာ ခိုင် နှုန်း ")
            print(f"တစ် မျိုး သား လုံး ၏ ပြည် တွ င်း အ သား တင် ထုတ် လုပ် မှု နှင့် ဝန် ဆော င် မှု တန် ဖိုး  :         {self.one_value}:           100")
            print(f"ပြည် ပ သွ င်း ကုန် တန် ဖိုး                                            :         {self.two}:             {two_persentage}")
            print(f"ပြည် ပ ပို့ ကုန် တန် ဖိုး                                             :         {self.three}:              {three_persentage}")
            print(f"ပြည် တွ င်း သုံး ရန် လက် ကျန်                                         :         {four}:           {four_persentage}")
            print(f"စား သုံး ရင် လျာ ထား သည့် တန် ဖိုး                                   :         {self.five}:           {five_persentage}")
            print(f"ငွေ ရင်း နှီး မြှပ် နှံ ရန် လျာ ထား သည့် တန် ဖိုး                          :         {self.six}:           {six_persentage}")
            print(f"ကုန် ပစ္စည်း လက် ကျန်                                              :         {seven}:            {seven_persentage}")
            
            
        

if __name__ == '__main__':
    # print("တစ် မျိုး သား လုံး ၏ ပြည်တွင်း...")
    value_one = float(input("တစ် မျိုး သား လုံး ၏ ပြည် တွ င်း အ သား တင်...:   "))
    # prfloat("ပြည် ပ သွင်း ကုန် တန်ဖိုး ")
    value_two = float(input("ပြည် ပ သွ င်း ကုန် တန် ဖိုး:    "))
    # prfloat("ပြည် ပ ပို့ ကုန် တန် ဖိုး ")
    value_three = float(input("ပြည် ပ ပို့ ကုန် တန် ဖိုး:    "))
    local_value = value_one + value_two - value_three
    print(f"ပြည် တွ င်း သုံး ရန် လက် ကျန် {local_value}")
    # prfloat("စား သုံး ရင် လျာ ထား သည့် တန် ဖိုး ")
    value_five = float(input("စား သုံး ရင် လျာ ထား သည့် တန် ဖိုး:    "))
    # prfloat("ငွေ ရင်း နှီး မြှပ် နှံ ရန် လျာ ထား သည့် တန် ဖိုး")
    value_six = float(input("ငွေ ရင်း နှီး မြှပ် နှံ ရန် လျာ ထား သ ည့် တန် ဖိုး:   "))
    GDP = Utilization_of_GDP(value_one, value_two, value_three, value_five, value_six)
    GDP.main()
        
        