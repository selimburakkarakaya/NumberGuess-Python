import random
tahmin = random.randint(1,100)
# print(tahmin)
for i in range(0,6):
  sayi=int(input("Sayı Giriniz: "))
  if(sayi > tahmin):
    if(i >= 5):
      print("Tahmin hakkınız kalmadı." )
      print("Tutulan Sayı:", tahmin)
      break
    print("Cevabınız yanlış.", str(5-i) , "tahmin hakkınız kaldı.")
    print("Daha küçük bir sayı giriniz.")
  elif(sayi < tahmin):
    if(i >= 5):
      print("Tahmin hakkınız kalmadı.")
      print("Tutulan Sayı:", tahmin)
      break
    print("Cevabınız yanlış.", str(5-i) , "tahmin hakkınız kaldı.")
    print("Daha büyük bir sayı giriniz.")
  else:
    print("Tebrikler!", i+1, "tahminde bildiniz.")
    break