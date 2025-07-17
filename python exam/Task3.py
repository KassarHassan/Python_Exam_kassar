# Task 3
def count_vowels(text):               
    text_lower = text.lower()         
    vowels = ['a', 'e', 'i', 'o', 'u'] # list of vowels to count
    total = 0                         
    counts = {}                      
    for v in vowels:                  
        counts[v] = 0

    for ch in text_lower:            
        if ch in vowels:             
            counts[ch] += 1           
            total += 1                

    # print results
    print(f"Total vowels: {total}")   # total number of vowels
    for v in vowels:                  
        print(f"{v}: {counts[v]}")  

prompt_text = (
    "Today is my final exam of Python, "
    "It is an amazing laugange that i will keep on learning."
)
count_vowels(prompt_text)           

print()
