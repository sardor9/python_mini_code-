from math import floor
MAC = 'C46E1F6A8D04'
One = Two = (int(MAC, 16) & 0xFFFFFF) % 10000000
Var1 = 0
While Two:
  Var1 += 3 * (Two % 10)
  Two = floor(Two / 10)
  Var1 += Two % 10
  Two = floor(Two / 10)
Var2 = (One * 10) + ((10 - (Var1 % 10)) % 10)
Var3 = str(int(Var2))
result = Var3.zfill(8)