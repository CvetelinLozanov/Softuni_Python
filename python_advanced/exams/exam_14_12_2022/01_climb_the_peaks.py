from collections import deque


peaks = deque([[80, "Vihren"], [90, "Kutelo"], [100, "Banski Suhodol"], [60, "Polezhan"], [70, "Kamenitza"]])
peaks_counter = 0
portions = deque([int(portion) for portion in input().split(', ')])
stamina = deque(int(num) for num in input().split(', '))
conquered_peaks = []

while portions and stamina:
    current_portion = portions.pop()
    current_stamina = stamina.popleft()
    calculation = current_portion + current_stamina
    current_peak = peaks.popleft()

    if calculation >= current_peak[0]:
        conquered_peaks.append(current_peak[1])
    else:
        peaks.appendleft(current_peak)

    if not peaks:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break

else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks:")
    print('\n'.join(conquered_peaks))

