# nomor 1
with open("icecream.txt","r") as file:
    contents = file.read()
    print(contents)

salesdata={}
with open("icecream.txt", "r") as data:
    for line in data:
        if ":" in line:
            parts = line.strip().split(":")
            flavor = parts[0]
            sales = [float(part) for part in parts[1:]]
            salesdata[flavor] = sales

print(salesdata)


#nomor 2
Salesdata = {}
with open("icecream.txt", "r") as data:
    for line in data:
        if ":" in line:
            flavor, *sales = line.strip().split(":")  
            Salesdata[flavor] = [float(s) for s in sales]  

flavor_totals = {flavor: sum(sales) for flavor, sales in Salesdata.items()}

store_totals = [sum(sales) for sales in zip(*Salesdata.values())] 

print("Sales Report:")

print("\nSales by Flavor:")
for flavor, total_sale in sorted(flavor_totals.items()):
    print(f"{flavor}: {total_sale:.2f}")

print("\nSales by Store:")
for i, store_sale in enumerate(store_totals):
    print(f"Store {i+1}: {store_sale:.2f}")


#nomor 3
def analyze_text(text_file, word_file):

  with open(text_file, 'r') as f:
    text = f.read().lower()  

  import re
  words = re.findall(r'\w+', text)

  word_count = len(words)
  unique_word_count = len(set(words))

  with open(word_file, 'r') as f:
    correctly_spelled_words = set(line.strip().lower() for line in f) 

  misspelled_words = [word for word in words if word not in correctly_spelled_words]

  return {
      'word_count': word_count,
      'unique_word_count': unique_word_count,
      'misspelled_words': misspelled_words
  }

results = analyze_text("alice.txt", "words.txt")

print(f"Count Word: {results['word_count']}")
print(f"Unique Word: {results['unique_word_count']}")
print(f"Missspelled Word: {results['misspelled_words']}")