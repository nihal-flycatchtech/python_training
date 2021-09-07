def main(num):
    file = open("D:\python\prime_or_not.txt", 'w')
    file.write("\nfunction with parameter to perform prime or not")


    file.write("\ndefine a flag variable")
    flag = False


    file.write("\nprime numbers are greater than 1")
    if num > 1:

        file.write("\ncheck for factors")
        for i in range(2, num):
            if (num % i) == 0:

                file.write("\nif factor is found, set flag to True")
                flag = True

                file.write("\nbreak out of loop")
                break


    file.write("\ncheck if flag is True")
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

main(4)