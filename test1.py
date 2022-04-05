



def younger_person():
  ages = [72,42,32,50,56,14,78,30,51,89,12,38,67,10]

  solution = ages[0]
  for age in ages:
    if age < solution:
      solution = age

  print(solution)


def statistics():
  data = [12,-1,123,345,412,4.55,123,23.4,123,4587,-129,94,956,14565,32, 0.001, 123]

  negative = 0
  count = 0
  total = 0
  over_500 = 0
  for num in data:
    # count = count + 1
    count += 1
    # total = total + num
    total += num

    if(num > 500):
      over_500 += 1

    if num < 0:
      negative = negative + num # or + 1 gives how many neg nums

  print(over_500)
  print(f"3 solution is: {negative}")
  print(f"1 solution is: {count}") 
  print(f"1 solution is: {len(data)}") # same as prior line
  print(f"2 solution is: {total}")
  print(f"2 solution is: {sum(data)}") # same as prior line
  
  print(len("Hello World"))



def print_some_nums():
  # print numbers from 10 to 100
  for n in range(1, 11):
    print(n*10)

  for x in range(10,110,10):
    print(x)


print_some_nums()



print("Test test test")
younger_person()
statistics()
