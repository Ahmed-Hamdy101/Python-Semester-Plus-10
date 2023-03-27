# list argument its arguments as list of arrays
def main():
    voice("Meow.....","woof","OOOOOW")

def voice(**kwargs):
    if len(kwargs):
        for i in kwargs:
            print(i)
    else:
        print("single line...")


# main function that execute the code and note also we can import this code inside a file
if __name__== '__main__':main()
