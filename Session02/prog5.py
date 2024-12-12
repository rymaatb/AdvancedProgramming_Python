score_houma = int(input("please type in score tae el houma: "))
score_baraniya = int(input("please type in score tae el baraniya: "))
while (score_baraniya<0 or score_houma<0):
    score_houma = int(input("please type in score tae el houma:"))
    score_baraniya = int(input("please type in score tae el baraniya"))
if score_baraniya == score_houma:
        print(f"It was a tie!")
elif score_houma > score_baraniya :
        print(f"El houma wins the game!!!")
else:
        print(f"Baraniya wins the game! (match mabyo3)")
