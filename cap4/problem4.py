__author__ = 'raluca.garba'

# Time spent at routers
# Given data: Traceroute from Birmingham, England to Sundwall, Sweeden takes 75 ms.
# The distance between Birmingham and Sundwall is 2500 km.
# The speed of light in optical fibre is 200.000 km/s.
# 1 s = 1000 ms
# Q: What is the total time spent at the routers?


total_time = 75 # ms
distance = 2500 # km
optic_speed = 200000.0 #km/s
ms_per_s = 1000

#Calculation:
time_on_wires = 2 * distance * ms_per_s / optic_speed # [km/s]*[ms/s]/[km]
routers_time = total_time - time_on_wires

print routers_time