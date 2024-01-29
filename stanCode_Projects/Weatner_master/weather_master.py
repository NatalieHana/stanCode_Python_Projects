"""
File: weather_master.py
Name: Natalie
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100  # Sentinel value


def main():
	"""
	This program finds minimum, maximum, average temperature among user inputs
	and conclude how many days temperature below 16C as cold day
	"""
	print("stanCode \"Weather Master 4.0\"!")
	temperature = []
	temp = int(input("Next Temperature: (or" + str(EXIT) + "to quit)?"))
	if temp == EXIT:
		print("No temperature were entered")
	else:
		maximum = temp
		minimum = temp
		while True:
			temperature.append(temp)  # 將溫度加到列表中
			temp = int(input("Next Temperature: (or -100 to quit)?"))
			if temp == EXIT:
				break
			elif temp > maximum:
				maximum = temp
			elif temp < minimum:
				minimum = temp
		print("Highest temperature =" + str(maximum))
		print("Lowest temperature =" + str(minimum))

		# 計算平均溫度
		average = float(sum(temperature) / len(temperature))
		print("Average =" + str(average))

		# 計算小於16度C的天數
		cold_days = len([temp for temp in temperature if temp < 16])
		print(str(cold_days) + " cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
