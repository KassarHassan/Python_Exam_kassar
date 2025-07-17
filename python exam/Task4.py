#Task 4:
import numpy as np                    # import numpy for average calculation

numbers = []                          # list to store user-entered numbers
while True:                           # infinite loop until break
    entry = input("Enter a number or 'done': ").strip()  # get user input
    if entry.lower() == 'done':       # check if user wants to stop
        break                         # exit loop
    if entry == '':                   # skip empty inputs
        print("Invalid input. Try again.")  
        continue
    try:
        num = float(entry)            
        numbers.append(num)           
    except ValueError:
        print("Invalid input. Try again.")  # notify invalid


count = len(numbers)                 
if count > 0:                       
    avg = np.mean(numbers)        
    print(f"You entered {count} values.")  
    print(f"Average: {avg:.2f}")     
else:
    print("No numbers entered.")      

print() 
