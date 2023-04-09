inp = input("do you want to stop")
while inp != 'stop':

 	input1 = int(input("while number multipliction do you want?"))
 	input2 = int(input("upto which number you want it to run?"))

 	for i in range(input2):
 		print(f"{i} X {input1} = {i * input1")
 	inp = input("which number multipaltion do you want?")