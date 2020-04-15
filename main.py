from urban_planner import Building
from urban_planner import rolling_hills1
from urban_planner import rolling_hills2
from urban_planner import rolling_hills3
from urban_planner import rolling_hills4
from urban_planner import rolling_hills5




from city import City

# Create a new city instance and add your building instances to it.
#  Once all buildings are in the city, iterate the city's building 
#  collection and output the information about each building in the city.

megalopolis = City("megalopolis", "mayor", 1991)

megalopolis.all_buildings.append(rolling_hills1)
megalopolis.all_buildings.append(rolling_hills2)
megalopolis.all_buildings.append(rolling_hills3)
megalopolis.all_buildings.append(rolling_hills4)
megalopolis.all_buildings.append(rolling_hills5)


for building in megalopolis.all_buildings:
   building.printBuildingDetails()