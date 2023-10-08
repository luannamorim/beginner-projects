import os


def main():
    i = 0
    path = "C:/Users/Luann/OneDrive/teste/"

    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg"
        my_source = path + filename
        my_destf = path + my_dest
        os.rename(my_source, my_destf)
        i += 1
        print(filename, ">", my_dest)


if __name__ == '__main__':
    main()
