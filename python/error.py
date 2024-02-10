try:
    f = open('myfile.txt', 'w') # you can change the second paramenter to take in an r for only read and w to write
    f.write("Welcome to the new File.")
except IOError as ioe:
    print(f"Error: {ioe}")
else:
    print("SUCCESS!")
    f.close()
finally:
    print("Any code inside of the finally will print or get executed.")
