import time

print("starting OS")
time.sleep(1)
print("loading...")
time.sleep(0.5)
ram1 = "32mb"
rom1 = "100mb"
print("RAM:" + ram1)
print("ROM:" + rom1)
time.sleep(1)
print("Virtual OS")
print("v/1.0")
print("write info")
while True:
	command1 = input("Enter command: ")
	if command1 == "systeminfo":
		print("VirtualOSv1.0")
		print("beta version")
	if command1 == "calculator":
		calc1 = float (input("Введите 1-ое число: "))
		calc2 = float (input("Введите 2-ое число: "))
		calc3 = input("Что хотите сделать(+,-,/,*): ")
		if calc3 == "+":
			answer1 = (calc1 + calc2)
			print(str(answer1))
			print("решено")
		if calc3 == "-":
			answer1 = (calc1 - calc2)
			print(str(answer1))
			print("решено")
		if calc3 == "/":
			answer1 = (calc1 / calc2)
			print(str(answer1))
			print("решено")
		if calc3 == "*":
			answer1 = (calc1 * calc2)
			print(str(answer1))
			print("решено")
	if command1 == "info":
		print("Commands:")
		print("calculator")
		print("systeminfo")
