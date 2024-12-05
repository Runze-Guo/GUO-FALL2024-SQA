import secrets

def divide(v1, v2):
   try:
       return v1 / v2
   except ZeroDivisionError:
       print("Error: Attempt to divide by zero.")
       return None  # Return None in case of division by zero

def getItem(data, index):
   try:
       return data[index]
   except IndexError:
       print(f"Error: Index {index} out of range.")
       return None  # Return None if the index is out of range

def absValue(number):
   if not isinstance(number, (int, float)):  # Ensure number is a valid type
       print("Error: Input must be a number.")
       return None
   if number < 0:
      raise ValueError("Input must be non-negative")
   return number

def sumList(numbers):
   if not all(isinstance(num, (int, float)) for num in numbers):  # Check if all items are numbers
       print("Error: List contains non-numeric values.")
       return None
   total = 0
   for num in numbers:
      total += num
   return total

def isUpperCase(char):
   if not isinstance(char, str) or len(char) != 1:  # Ensure it's a single character
       print("Error: Input must be a single character string.")
       return False
   return char.isupper()

def fuzzValues(val1, val2):
   if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):  # Check input types
       print("Error: Both inputs must be numeric.")
       return None
   return divide(val1, val2)

def simpleFuzzer1():
    ls_ = ['123', 'True', 'False', [], None, '/', '2e34r']
    for x in ls_:
      print(f"Testing: {x}")
      if isinstance(x, str):
         mod_x = x + str(secrets.randbelow(10))
      elif isinstance(x, int):
         mod_x = x + secrets.random()
      try:
         result = fuzzValues(x, mod_x)
         if result is not None:
            print(f"Result of fuzzValues: {result}")
      except Exception as e:
         print(f"Error in fuzzValues: {e}")

def simpleFuzzer2():
   data = [1, 2, 3]
   index = 4
   print(f"Data: {data}, Index: {index}")
   try:
      element = getItem(data, index)
      if element is not None:
         print(f"Element at index {index}: {element}")
   except Exception as e:
      print(f"Error in getItem: {e}")

def simpleFuzzer3():
   value = -4
   print(f"Testing absValue: {value}")
   try:
      result = absValue(value)
      if result is not None:
         print(f"Absolute value: {result}")
   except Exception as e:
      print(f"Error in absValue: {e}")

def simpleFuzzer4():
   data = ["1", 2, 3]
   print(f"Testing sumList: {data}")
   try:
      result = sumList(data)
      if result is not None:
         print(f"Sum of list: {result}")
   except Exception as e:
      print(f"Error in sumList: {e}")

def simpleFuzzer5():
   data = ['A', 'b', 'C']
   print(f"Testing isUpperCase: {data}")
   for char in data:
      try:
         result = isUpperCase(char)
         print(f"Character {char} is upper case: {result}")
      except Exception as e:
         print(f"Error in isUpperCase: {e}")

if __name__=='__main__':
    simpleFuzzer1()
    simpleFuzzer2()
    simpleFuzzer3()
    simpleFuzzer4()
    simpleFuzzer5()
