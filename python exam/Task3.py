# --- Task 3: Define count_vowels(text) ---
def count_vowels(text):               # function takes a string
    text_lower = text.lower()         # convert text to lowercase for uniformity
    vowels = ['a', 'e', 'i', 'o', 'u'] # list of vowels to count
    total = 0                         # initialize total vowel counter
    counts = {}                       # dict to hold counts per vowel
    for v in vowels:                  # initialize each vowel count to zero
        counts[v] = 0

    for ch in text_lower:             # iterate over each character in text
        if ch in vowels:              # check if character is a vowel
            counts[ch] += 1           # increment count for that vowel
            total += 1                # increment total counter

    # print results
    print(f"Total vowels: {total}")   # total number of vowels
    for v in vowels:                  # for each vowel
        print(f"{v}: {counts[v]}")    # how many times it appeared

# String from prompt
prompt_text = (
    "Today is my final exam of Python, "
    "It is an amazing laugange that i will keep on learning."
)
count_vowels(prompt_text)             # call vowel counter

print()