import time
import random
import matplotlib.pyplot as plt
import pandas as pd

# Simulating data collection from sensors
def collect_data():
    timestamp = time.time()
    energy_consumption = random.uniform(10, 100)
    return {'timestamp': timestamp, 'energy_consumption': energy_consumption}

# Initialize data storage
data_history = []

# Simulate data collection over time
for _ in range(100):
    data_point = collect_data()
    data_history.append(data_point)
    time.sleep(1)  # Simulate real-time data collection interval

# Create a Pandas DataFrame from the collected data
df = pd.DataFrame(data_history)

# Calculate daily energy consumption
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
df.set_index('timestamp', inplace=True)
daily_energy = df['energy_consumption'].resample('D').sum()

# Visualize daily energy consumption
plt.figure(figsize=(10, 6))
daily_energy.plot(kind='bar')
plt.title('Daily Energy Consumption')
plt.xlabel('Date')
plt.ylabel('Energy Consumption')
plt.show()
