def check_password_validity(password: str, letter: str, low: int, high: int):
    char1 = password[low - 1] == letter
    char2 = password[high - 1] == letter
    
    if char1 + char2 is not 1:
        return False    
    return True

def get_range(param: str):
    minmax = param.split('-')
    return int(minmax[0]), int(minmax[1])

def is_valid(line: str):
    params = line.split(' ')
    low, high = get_range(params[0])
    password: str = params[2].strip()
    letter: str = params[1].strip()[0]     
    if (check_password_validity(password, letter, low, high)):
        return 1    
    return 0    

num_valid = 0
f = open("input.txt")
for line in f:
    num_valid += is_valid(line)

print(num_valid)