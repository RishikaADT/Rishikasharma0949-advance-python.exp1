import numpy as np
heart_rate = np.random.randint(80,151,10)

print("Heart rates for 10 minutes:")
print(heart_rate)

first_5_minutes=heart_rate[:5]
print("\nheart rates during first 5 mintues:")
print(first_5_minutes)

maximum = np.max(heart_rate)

minimum = np.min(heart_rate)

average = np.mean(heart_rate)

print("\nMaximum heart rate:", maximum,"BPM")
print("Minimum heart rate:",minimum,"BPM")
print("average heart rate:", round(average,2),"BPM")

high_rate = heart_rate > 120

print("\nHeart rates exceeding 120 BPM:")
print(heart_rate[high_rate])

minutes = np.where(heart_rate > 120) [0] + 1

print("\nMinutes where heart rate exceeded 120 BPM:")
print(minutes)












