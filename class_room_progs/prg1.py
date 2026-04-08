import pandas as pd
s=pd.Series(['10','20','abc','30'])
numeric_s=pd.to_numeric(s,errors='coerce')
print(numeric_s)

# Converts value to int or float tries to interpret each string as a number note error is equal to course this is the key concept if conversion is possible convert 
# convert possible conversion is if  is the key concept his course to equal error is number note a string as interpret each to  trif conversion is possible convert 