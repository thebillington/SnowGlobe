from snowglobe import *

snowglobe = Snowglobe("Snowman Globe", 50)

while True:

    if snowglobe.snowHeight < 200:
        snowglobe.snowHeight += 1
        
    snowglobe.update()
