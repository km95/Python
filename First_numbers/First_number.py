def first_number():
    print("Write a numbers of tests : ")
    amount_tests = 0
    try:
        amount_tests = int(input())
    except ValueError:
        print("It is not number")
    tab_amount = []
    while amount_tests != 0:
        print("Write numbers : ")
        number = 0
        try:
            number = int(input())
        except ValueError:
            print("It is not number")
        tab_amount.append(number)
        amount_tests -= 1

    counter = len(tab_amount)

    while counter != 0:
        counter_number = 1
        counter_breaker = 0
        if tab_amount[counter - 1] == 1:
            print("%d - YES" % (tab_amount[counter - 1]))
            counter -= 1
            continue

        while tab_amount[counter - 1] != counter_number:

            if (tab_amount[counter - 1] % counter_number) == 0:
                counter_breaker += 1

            if counter_breaker >= 2:
                print("%d - NO " % (tab_amount[counter - 1]))
                break

            counter_number += 1

            if tab_amount[counter - 1] == counter_number:
                print("%d - YES" % (tab_amount[counter - 1]))

        counter -= 1
