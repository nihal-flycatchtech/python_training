def main(num):
    file = open("D:\python\prime_or_not.txt", 'w')
    file.write("\nfunction with parameter to perform prime or not")
    if num>1:
        file.write("\ncheck num greater than 1")
        for i in range(2,num):
            file.write("\niterate from 2 to num")
            if (num%i)==0:
                file.write("\ncheck num is divisible by i ")
                print("it is not a prime number")
                file.write("\nprint not prime number ")
                break
        else:
            file.write("\nif num is not divisible by i ")
            print("its a prime number")
            file.write("\nprint prime number ")
    else:
        file.write("\nif num is less than 1")
        print("its not a prime number")
        file.write("\n print not prime number ")
main(13)