fileName = input("Enter a file path aka 'C:\PythonTestFile.txt': ")
with open(fileName, 'r') as fin:
    print (fin.read())