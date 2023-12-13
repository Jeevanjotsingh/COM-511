def write_to_file(file_name):
    try:
        with open(file_name, 'w') as file:
            for i in range(3):
                line = input(f"Enter line {i + 1}: ")
                file.write(line + '\n')
        print(f"Content written to '{file_name}' successfully.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


def main():
    file_name = "MyFile.txt"
    write_to_file(file_name)


if __name__ == "__main__":
    main()