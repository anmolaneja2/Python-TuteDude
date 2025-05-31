string=input("Enter text to write to the file: ")

with open("sample2.txt","w") as file:
    file.write(string +"\n")

string2=input("Enter additional text to append: ")

with open("sample2.txt","a") as file:
    file.write(string2+ "\n")


print("Final content of output.txt: ")
with open("sample2.txt","r") as file:
    for i,line in enumerate(file, start=1):
        print(f"{line.strip()}")