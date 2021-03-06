# NEEDED INFO. Metrics needing updated for each operation.
vwp = 70
max_tbrd = 6
number_suspect = 5


# NEEDED INFO. Animals to check with cooresponding records. 
# 4 quantitative and 1 qualitative (current visual oberservation) metrics.
# Paint score is the amount of tail chalk currently on the animal 0 (none) - 3 (100%).
# Import quantiative metrics from DC305 or other management software. 
# rc (repro code): 1= DNB, 2= Fresh, 3= Open, 4= Bred, 5= Preg, 6= Dry
cow_1 = 13267
dim_1 = 75
tbrd_1 = 1
dslh_1 = 18
rc_1 = 4
paint_score_1 = 1

cow_2 = 14890
dim_2 = 49
tbrd_2 = 0
dslh_2 = 0
rc_2 = 4
paint_score_2 = 0

cow_3 = 12632
dim_3 = 220
tbrd_3 = 5
dslh_3 = 22
rc_3 = 5
paint_score_3 = 2

cow_4 = 11765
dim_4= 92
tbrd_4 = 2
dslh_4 = 36
rc_4 = 4
paint_score_4 = 3

cow_5 = 11355
dim_5 = 120
tbrd_5 = 3
dslh_5 = 11
rc_5 = 4
paint_score_5 = 1


# Create list for each animal.
check_cow_1=[cow_1, dim_1, tbrd_1, dslh_1, rc_1, paint_score_1]
check_cow_2=[cow_2, dim_2, tbrd_2, dslh_2, rc_2, paint_score_2]
check_cow_3=[cow_3, dim_3, tbrd_3, dslh_3, rc_3, paint_score_3]
check_cow_4=[cow_4, dim_4, tbrd_4, dslh_4, rc_4, paint_score_4]
check_cow_5=[cow_5, dim_5, tbrd_5, dslh_5, rc_5, paint_score_5]


# Perform AI Confidence Analysis and print insights.
def check_this_cow(ID):
    if ID[2]>= 6:
      recommendation = "Do Not Breed"
      insights = "Bred too many times"
               # TBRD>6
    elif ID[4] == 1:
      recommendation = "Do Not Breed"
      insights = "Repro code = DNB"
               # RC=DNB
    elif ID[1] < vwp:
      recommendation = "Do Not Breed"
      insights = f"Animal's DIM is too low, wait until the VWP of {vwp}"
               # <VWP
    elif ID[4] >= 5: 
      if ID[5] <= 1:
        recommendation = "Palpate to ensure open, then breed"
        insights = "She is pregnant in the computer, but if she is open go for it"
      else:
        recommendation = "Do Not Breed"
        insights = "Pregnant"
    elif ID[3] <14:
      recommendation = "Do Not Breed"
      insights = "Service interval is too low"
    elif ID[3] >= 14 and ID[3] <= 25 and ID[5] == 3:
      recommendation = "Do Not Breed"
      insights = "Not enough painted rubbed off"
    elif ID[3] > 25 and ID[5] >= 2:
      recommendation = "Do Not Breed"
      insights = "Repaint"
    else: 
      recommendation = "Good to breed"
      insights = "Make sure to deposit slowly"
   
    print(f"Cow ID = {ID[0]}")
    print(f"DIM: {ID[1]}, TBRD: {ID[2]}, DSLH: {ID[3]}, RC: {ID[4]}, Paint score: {ID[5]}")
    print(f"Recommendation: {recommendation}")
    print(f"Insights: {insights}")
    print("")


# Print Header
print("~~~~~ Breed List ~~~~~")
print("")  
print("Suspect heats:")
print(f"Total count = {number_suspect}")
print("")


# Run and print analysis for each animal 
check_this_cow(check_cow_1)
check_this_cow(check_cow_2)
check_this_cow(check_cow_3)
check_this_cow(check_cow_4)
check_this_cow(check_cow_5)