# Katelyn Curtiss
# January 8 2025

def get_city():
    city = input("Enter the city you live in:")
    return city

def get_age():
    age = input("Enter your age:")
    return age

def build_output(city, age):
    output =  f"You live in {city} and you are {age} years old."
    return output

def main():
    city = get_city()
    age = get_age()

    result = build_output(city, age)

    print(result)
if __name__ == "__main__": 
  main()