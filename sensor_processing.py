def calculate_average(values):
    """Return the average of a list of numbers."""
    return sum(values) / len(values)
data = [72, 55, 101, 90]
print("Average:", calculate_average(data))
stations = [
    ["A1", 62],
    ["B5", 97],
    ["C3", 155]
]
for station in stations:
    print(f"{station[0]} → {station[1]}")
  def report_status(stations, threshold):
    """
    For each [id, pm25] in stations:
    print "id → pm25 µg/m^3 (safe)" if pm25 < threshold,
    else "(danger!)"
    """
    for station in stations:
        station_id, pm25 = station
        if pm25 < threshold:
            print(f"{station_id} → {pm25} µg/m³ (safe)")
        else:
            print(f"{station_id} → {pm25} µg/m³ (danger!)")
stations = [
    ["A1", 62],
    ["B5", 97],
    ["C3", 155]
]
report_status(stations, 100)
