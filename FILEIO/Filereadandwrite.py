file = open(r'C:\Users\Roshni\PycharmProjects\pythonProject2\examples\fdg.txt', 'r')
#print(file.read())
content = (file.readlines())
for i in content:
    print(i)
file.close()

# with open("roshni.txt",'a') as file:
#     file.write("God is Great")
