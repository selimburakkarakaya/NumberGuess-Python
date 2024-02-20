import random

print("Cevap doğruysa - 0'a basınız.")
print("Cevap daha küçük bir sayı ise - 1'e basınız.")
print("Cevap daha büyük bir sayı ise - 2'ye basınız.")
x = 1
y = 100
for i in range(0, 8):
  # tahmin = random.randint(x, y) # bu yöntemle daha fazla hak kullanarak buluyor. ya da 8 hakta bulamayabiliyor.
  tahmin = int((x + y)/2)
  print("Tahmin:", tahmin, "doğru mu?")
  cevap = int(input("Cevap: "))
  if cevap == 1:
    if i >= 7:
      print("Tahmin hakkınız kalmadı. Tekrar deneyiniz." )
      break
    y = tahmin -1
    print(str(7-i) , "tahmin hakkınız kaldı.")
    print("Daha küçük bir sayı giriniz.")
  elif cevap == 2:
    if i >= 7:
      print("Tahmin hakkınız kalmadı. Tekrar deneyiniz.")
      break
    x = tahmin +1
    print(str(7-i) , "tahmin hakkınız kaldı.")
    print("Daha büyük bir sayı giriniz.")
  elif cevap == 0:
    print("Tebrikler!", i+1, "tahminde bildiniz.")
    break
  
  