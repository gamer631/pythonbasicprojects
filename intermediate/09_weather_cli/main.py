"""Get current weather from Open-Meteo using latitude and longitude."""
import argparse, json
from urllib.request import urlopen
from urllib.error import URLError

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('latitude',type=float); p.add_argument('longitude',type=float); a=p.parse_args()
    url=f'https://api.open-meteo.com/v1/forecast?latitude={a.latitude}&longitude={a.longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=auto'
    try:
        with urlopen(url,timeout=12) as response: data=json.load(response)
    except (URLError,TimeoutError,ValueError) as exc: p.error(f'Weather request failed: {exc}')
    current=data.get('current',{}); units=data.get('current_units',{})
    print('Current weather')
    print(f'Temperature: {current.get("temperature_2m", "n/a")} {units.get("temperature_2m", "")}')
    print(f'Humidity: {current.get("relative_humidity_2m", "n/a")}%')
    print(f'Wind: {current.get("wind_speed_10m", "n/a")} {units.get("wind_speed_10m", "")}')
    print('Updated:',current.get('time','unknown'))
if __name__=='__main__': main()
