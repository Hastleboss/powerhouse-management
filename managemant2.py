import random
import time

class EnergyManagementSystem:
    def __init__(self):
        self.energy_consumption = 0
        self.setpoint = 100  # Desired energy consumption level

    def monitor_energy_consumption(self):
        # Simulate reading energy consumption from sensors
        self.energy_consumption = random.uniform(80, 120)
        print(f"Current energy consumption: {self.energy_consumption}")

    def control_strategy(self):
        # Basic control strategy: adjust based on deviation from setpoint
        deviation = self.energy_consumption - self.setpoint
        if deviation > 10:
            print("Reducing energy usage...")
            # Implement control logic here (e.g., adjust HVAC, lighting, etc.)

    def run(self):
        while True:
            self.monitor_energy_consumption()
            self.control_strategy()
            time.sleep(5)  # Simulate a 5-second interval

if __name__ == "__main__":
    ems = EnergyManagementSystem()
    ems.run()
