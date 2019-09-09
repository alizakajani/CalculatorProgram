def check_HDL(HDL_result):
	if HDL_result >= 60:
		return "Normal"
	elif 40 <= HDL_result < 60:
		return "Borderline low"
	else:
		return "low"

def interface():
	print("My calculator program")
	keep_running = True
	while keep_running:
		print("Option: ")
		print("9 - Quit")
		choice = input("Enter your choice: ")	# input returns a string
		if choice == '9':
			keep_running = False
	return

if __name__ == "__main__":
	interface()