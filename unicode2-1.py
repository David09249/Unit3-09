# Created by : David Wang
# Created on : 24 Oct 2017
# Created for : ICS3UR
# Daily Assignment - Unit3-09
# This program displays every lowercase letter for each uppercase letter

for index_A in range(65, 91):
    for index_a in range(97, 123):
        print(unichr(index_A) + '     >     ' + unichr(index_a))
