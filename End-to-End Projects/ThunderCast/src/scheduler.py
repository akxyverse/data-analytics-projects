from apscheduler.schedulers.blocking import BlockingScheduler
from data_collection import fetch_weather_data
import logging

logging.basicConfig(level=logging.INFO)

scheduler = BlockingScheduler()

# Schedule to run every hour
scheduler.add_job(fetch_weather_data, 'interval', hours=1)

print("⏰ Weather data collection scheduler started!")
print("Collecting data every 1 hour...")
print("Press Ctrl+C to stop")

# Run immediately on start
fetch_weather_data()

# Start scheduler
scheduler.start()