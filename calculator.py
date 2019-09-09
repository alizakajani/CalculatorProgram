def interface():
	print("My calculator program")
	print("Option: ")
	print("9 - Quit")
	choice = input("Enter your choice: ")	# input returns a string
	if choice == '9':
		return

if __name__ == "__main__":
	interface()