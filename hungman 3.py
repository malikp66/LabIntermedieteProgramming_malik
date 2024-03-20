def updateText(secretWord, guessed_letters): #fungsi untuk kondisi benar/salah dalam displaynya
   display = "" #inisiasi string kosong
   for letter in secretWord:
    if letter.isalpha(): #ini buat spasi dimana kalo kondisinya bukan huruf maka kondisi jadi ke false 
       if letter.lower() in guessed_letters:
           display += letter #kalo ada huruf dalam secretword nampilin serta nambahin letternya
       else:
           display += "_"
    else:
        display += letter
   return display

#variabel global didefinisikan
secretWord = "Anak Software" 
guessed_letters = []
chances = 6

while chances > 0: #ini untuk looping chances nya sebanyak berapa kali
   guess = input("Guess a letter in my secret word: ")
   if len(guess) != 1 or not guess.isalpha(): 
       print("Please give me one letter.")
   elif guess.lower() in guessed_letters:
       print("You already guessed that letter.")
   else:
       guessed_letters.append(guess.lower())
       if guess.lower() in secretWord.lower(): #jika huruf masuk ke dalam secretword 
           print(f"Congrats, {guess} is in the secret word!")
       else:
           chances -= 1
           print(f"Better luck next time. You have {chances} chances left.") 

   display = updateText(secretWord, guessed_letters)
   print(display)

   if "_" not in display:
       print(f"Congratulations! You guessed the word: {secretWord}")
       break

if chances == 0:
   print(f"Sorry, you ran out of chances. The word was: {secretWord}")