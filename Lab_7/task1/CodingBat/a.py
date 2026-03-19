def sleep_in(weekday, vacation):
  return not weekday or vacation

def diff21(n):
    if n <= 21:
        return abs(n - 21)
    else:
        return 2 * abs(n - 21)
    
def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False
    
def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10

def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)
    
def not_string(s):
    if s.startswith("not"):
        return s
    else:
        return "not " + s
    
def missing_char(s, n):
    return s[:n] + s[n+1:]

def front_back(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]

def front3(s):
    front = s[:3]
    return front * 3

def sum_double(a, b):
  if (a == b):
    return a*4
  return a+b

def string_times(str, n):
  return str * n

def front_times(s, n):
    front = s[:3]
    return front * n

def string_bits(s):
    return s[::2]