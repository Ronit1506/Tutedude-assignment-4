try:
     file =open("sample.txt","rt")
     for line  in file:
        print(line.strip())
     file.close()
except FileNotFoundError:
    print(f"Error: {file} file not found.")

