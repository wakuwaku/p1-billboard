# p1-billboard
p1-billboard reads from Domoticz host and shows power usage numbers with tkinter
prerequisite: P1 cable connected and activated in Domoticz. Domoticz idx for power counter. 
Also shows costs per 24 hours and the current time.
USAGE:
# python3 -u p1-bilboard.py <domoticz ip address> <domotiz port> <idx> <kwh price>
# E.G.
# python3 -u p1-bilboard.py 10.0.1.100 8080 83 100.5
