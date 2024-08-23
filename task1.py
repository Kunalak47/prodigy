def celsius_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
  """Converts Celsius to Kelvin."""
  return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
  """Converts Fahrenheit to Kelvin."""
  return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
  """Converts Kelvin to Celsius."""
  return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
  """Converts Kelvin to Fahrenheit."""
  return (kelvin - 273.15) * 9/5 + 32

def main():
  """Prompts the user for a temperature value and unit, then converts and displays the temperature in other units."""
  while True:
    try:
      temperature = float(input("Enter the temperature value: "))
      unit = input("Enter the original unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

      if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        print(f"{temperature} degrees Celsius is equal to:")
        print(f"{fahrenheit:.2f} degrees Fahrenheit")
        print(f"{kelvin:.2f} Kelvin")
      elif unit == 'F':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        print(f"{temperature} degrees Fahrenheit is equal to:")
        print(f"{celsius:.2f} degrees Celsius")
        print(f"{kelvin:.2f} Kelvin")
      elif unit == 'K':
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        print(f"{temperature} Kelvin is equal to:")
        print(f"{celsius:.2f} degrees Celsius")
        print(f"{fahrenheit:.2f} degrees Fahrenheit")
      else:
        print("Invalid unit of measurement. Please enter C, F, or K.")
    except ValueError:
      print("Invalid temperature value. Please enter a number.")
    
    if input("Do you want to convert another temperature (y/n)? ").lower() != 'y':
      break

if __name__ == "__main__":
  main()