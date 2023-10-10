# x = "2000000458021"
# x = "2000000025476"
# x = "2000000025278"

# CHECK IF BARCODE 12 OR 13 DIGIT // ERROR HANDELING // GIT UPLOAD

a = 'yes'

while a == 'y' or a == 'yes':
    while True:
        try:
            x = int(input('Please enter 12 or 13 digit barcode in full: '))
            
            x = str(x)
            
            if len(x) == 12 or len(x) == 13:
                break
            else:
                print('=== Please enter a number which is 12 or 13 digits ===')
                continue
        except:
            print('=== Please enter a valid number ===')
            continue

    # # Split barcode number in to list
    # y = [int(i) for i in list(x)]

    # # Calculate sum of odd number placements
    # barcode_odd = sum(y[1::2])*3

    # # Calculate sum of even number placements
    # barcode_even = sum(y[:-1:2])

    # # Add sum of odd and even
    # check_digit_sum = barcode_odd + barcode_even

    # # Round sum to nearest 10
    # check_digit_round = rounded = round(check_digit_sum/10)*10

    # # Caluation to get check digit
    # if check_digit_sum > check_digit_round:
    #     check_digit = (check_digit_round + 10) - check_digit_sum
    # else:
    #     check_digit = check_digit_round - check_digit_sum
        
    # print(f"check digit = {check_digit}")

    a = input('Would you like to contuine or exit (y for "Yes" and n for "No"): ')