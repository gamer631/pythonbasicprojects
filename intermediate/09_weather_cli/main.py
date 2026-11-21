"""Fetch current weather for coordinates using Open-Meteo."""
import argparse
import json
from urllib.request import urlopen
from urllib.error import URLError



def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("latitude", type=float)
    parser.add_argument("longitude", type=float)
    args = parser.parse_args()
    url = ("https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=auto".format(args.latitude, args.longitude))
    try:
        with urlopen(url, timeout=10) as response:
            data = json.load(response)
    except (URLError, TimeoutError, ValueError) as exc:
        parser.error(f"Weather request failed: {exc}")
    current = data.get("current", {})
    print(f"Temperature: {current.get('temperature_2m', 'n/a')} {data.get('current_units', {}).get('temperature_2m', '')}")
    print(f"Humidity: {current.get('relative_humidity_2m', 'n/a')}%")
    print(f"Wind: {current.get('wind_speed_10m', 'n/a')} {data.get('current_units', {}).get('wind_speed_10m', '')}")
    print(f"Updated: {current.get('time', 'unknown')}")


if __name__ == "__main__":
    main()
