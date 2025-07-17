# --- Task 4: Collect numbers until 'done', then report count and average ---
import numpy as np                    # import numpy for average calculation

numbers = []                          # list to store user-entered numbers
while True:                           # infinite loop until break
    entry = input("Enter a number or 'done': ").strip()  # get user input
    if entry.lower() == 'done':       # check if user wants to stop
        break                         # exit loop
    if entry == '':                   # skip empty inputs
        print("Invalid input. Try again.")  # notify invalid
        continue
    try:
        num = float(entry)            # try converting to float
        numbers.append(num)           # store valid number
    except ValueError:
        print("Invalid input. Try again.")  # notify invalid

# after loop ends
count = len(numbers)                  # number of valid entries
if count > 0:                         # avoid division by zero
    avg = np.mean(numbers)            # compute average with numpy
    print(f"You entered {count} values.")  
    print(f"Average: {avg:.2f}")       # print average rounded to 2 decimals
else:
    print("No numbers entered.")      # if list was empty

print()  # blank line