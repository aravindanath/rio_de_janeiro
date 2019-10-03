
# w,a,a+ ---> new file will be created
# r, r+, ---> will throw an error as file doesnt exist

#   (PATH,MODE)
file = open("./TestData.txt","a+")

file.write("\nHowdy Ashwin")
file.close()





