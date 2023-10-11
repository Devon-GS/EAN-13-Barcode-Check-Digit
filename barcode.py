# ====== Barcodes For Testing ==========
# Barcode_1 = "2000000458021"
# Barcode_2 = "2000000025476"
# Barcode_3 = "2000000025278"
# =====================================

# While loop to check for error and valid barcode
a = 'yes'

while a == 'y' or a == 'yes':
    while True:
        try:
            print('=== To exit please type 0 (Zero) ===')
            x = int(input('Please enter 12 or 13 digit barcode in full: '))

            if x == 0:
                break
            
            x = str(x)
            
            if len(x) == 12 or len(x) == 13:
                break
            else:
                print('=== Please enter a number which is 12 or 13 digits ===')
                continue
        except:
            print('=== Please enter a valid number ===')
            continue

    if x == 0:
        break

    # Split barcode number in to list
    y = [int(i) for i in list(x)]

    # Calculate sum of odd number placements
    barcode_odd = sum(y[1::2])*3

    # Calculate sum of even number placements
    barcode_even = sum(y[:-1:2])

    # Add sum of odd and even
    check_digit_sum = barcode_odd + barcode_even

    # Round sum to nearest 10
    check_digit_round = rounded = round(check_digit_sum/10)*10

    # Caluation to get check digit
    if check_digit_sum > check_digit_round:
        check_digit = (check_digit_round + 10) - check_digit_sum
    else:
        check_digit = check_digit_round - check_digit_sum
        
    print(f"check digit = {check_digit}")

    a = input('Would you like to contuine or exit (y for "Yes" and n for "No"): ')