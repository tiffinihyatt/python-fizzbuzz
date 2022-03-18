# def fizzbuzz(number):

#     answer = []

#     for current_number in range(1, number + 1):
#         if current_number % 15 == 0:
#             answer.append("FizzBuzz")
#         elif current_number % 3 == 0:
#             answer.append("Fizz")
#         elif current_number % 5 == 0:
#             answer.append("Buzz")
#         else:
#             answer.append(str(current_number))
    
#     return answer

def fizzbuzz(number):
    # current_number = 15
    answer = []

    for current_number in range(1, number + 1):
        if current_number % 3 == 0 and current_number % 5 == 0:
            answer.append("FizzBuzz")
        elif current_number % 3 == 0:
            answer.append("Fizz")
        elif current_number % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(f"{current_number}")
    
    return answer