

reader_running = True

while reader_running:
	print("scan card now or type quit")

	card_no = int(input(": "))

	if card_no == "quit":
		reader_running = False
		break

	else: 
		print(card_no)

print("exiting...")