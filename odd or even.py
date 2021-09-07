enter_input=int(input("enter the limit"))
file=open("D:\python\odd_or_even.txt",'w')
file.write("recieved input")
empty_list=[]
file.write("\nempty list")

for i in range(enter_input):
    file.write("\niterate through the limit")
    c=int(input())
    file.write("\nrecieved list element")
    empty_list.append(c)
    file.write("\nappend to empty_list ")
even=list(filter(lambda n:n%2==0,empty_list))
file.write("\n lambda function to find the element in the list are even then convert  it to list ")
print("even number in the given list is",even)
odd=list(filter(lambda n:n%2!=0,empty_list))
file.write("\n lambda function to find the element in the list are odd then convert  it to list ")
print("odd number in the given list is",odd)