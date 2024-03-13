kata_rahasia = "malas"

huruf_user = input("Masukkan huruf: ").lower()

while len(huruf_user) != 1 and huruf_user.isalpha():
   print("Input yang anda masukkan tidak valid. Mohon masukkan satu buah huruf.")
   huruf_user = input("Masukkan huruf: ").lower()

if huruf_user in kata_rahasia:
   print("Huruf yang anda masukkan ada dalam kata rahasia")
else:
   print("Huruf yang anda masukkan tidak ada dalam kata rahasia")
