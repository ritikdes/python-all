import requests
import os
import json
import random

def search_country(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    cache_file = f"cache_{country_name.lower().strip().replace(" ", "_")}.json"

    if os.path.exists(cache_file):
        print("Loading from cache....")
        with open(cache_file, "r") as f:
            return json.load(f)

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 404:
            print(f"Country {country_name} not found.")
            return
        
        response.raise_for_status()
        data = response.json()[0]

        with open(cache_file, "w") as f:
            json.dump(data, f, indent=4)

        return data
    except requests.exceptions.ConnectionError:
        print("Connection error! Check your Internet connection.")
    except requests.exceptions.Timeout:
        print("The server took too long to respond. Try again later!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
   
    
def explore_region(region):
    url = f"https://restcountries.com/v3.1/region/{region}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 404:
            print(f"Region {region} not found.")
            return
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("Connection Error!")
    except requests.exceptions.Timeout:
        print("The server took too long to respond.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
    
def parse_country(data):
    country_info = {}
    country_info["official_name"] = data["name"]["official"]
    country_info["capital"] = data.get("capital", ["Unknown"])[0]
    country_info["population"] = data.get("population", 0)
    country_info["region"] = data.get("region", "Unknown")
    country_info["subregion"] = data.get("subregion", "Unknown")

    currencies = data.get("currencies", {})
    currency_list = []
    for code, info in currencies.items():
        name = info.get("name", "Unknown")
        symbol = info.get("symbol", "")
        currency_list.append(f"{name} ({symbol})")
    country_info["currency"] = ", ".join(currency_list) if currency_list else "Unknown"
    languages = data.get("languages", {})
    country_info["lang_list"] = list(languages.values())
    country_info["area"] = data.get("area")

    return country_info
    

def display_country(country_dict):
    official_name = country_dict["official_name"]
    capital = country_dict["capital"]
    population = country_dict["population"]
    region = country_dict["region"]
    subregion = country_dict["subregion"]
    currency = country_dict["currency"]
    languages = country_dict["lang_list"]
    area = country_dict["area"] 

    print("---------------------------------------")
    print(f"{'Official name':<15}: {official_name}")
    print(f"{'Capital':<15}: {capital}")
    print(f"{'Population':<15}: {population:,}")
    print(f"{'Region':<15}: {region}")
    print(f"{'Sub-region':<15}: {subregion}")
    print(f"{'Currency':<15}: {currency}")
    print(f"{'Languages':<15}: {languages}")
    print(f"{'Area':<15}: {f'{area:.2f} km²' if area else "Unknown"}")
    print("---------------------------------------")

    
def show_region_stats(countries):
    total_population = 0
    most_populous = max(countries, key=lambda x: x.get("population", 0))
    least_populous = min(countries, key=lambda x: x.get("population", 0))
    largest = max(countries, key=lambda x: x.get("area", 0))
    largest_name = largest.get("name",{}).get("common")
    largest_area = largest.get("area", 0)

    for c in countries:
        total_population += c.get("population",0)
    average_popn = total_population // len(countries)

    stats = {
        "most_pop_name": most_populous.get("name", {}).get("common"),
        "most_pop_val": most_populous.get("population"),
        "least_pop_name": least_populous.get("name", {}).get("common"),
        "least_pop_val": least_populous.get("population"),
        "total_popn": total_population,
        "average_popn": average_popn,
        "largest_name": largest_name,
        "largest_area": largest_area
    }
    return stats

def display_stats(region):
    countries = explore_region(region)

    if countries is None:
        print("Could not fetch region's data.")
        return
    
    stats = show_region_stats(countries)
    print(f"REGION {region.upper()} STATS")
    print("-"*40)
    countries_list = [c.get("name",{}).get("common") for c in countries]
    print(f"Countries: \n{countries_list}")
    print(f"{'Most Populous':<15}: {stats['most_pop_name']:<15} | {stats['most_pop_val']:,}")
    print(f"{'Least Populous':<15}: {stats['least_pop_name']:<15} | {stats['least_pop_val']:,}")
    print(f"{'Largest':<15}: {stats['largest_name']:<15} | {stats['largest_area']}")
    print(f"{'Total Population':<15}: {stats['total_popn']:,}")
    print(f"{'Average Population':<15}: {stats['average_popn']:,}")


def compare_countries(country1, country2):
    c1 = search_country(country1)
    c2 = search_country(country2)

    if c1 is None or c2 is None:
        print("Cannot compare because one or both countries do not exist.")
        return
    
    c1_info = parse_country(c1)
    c2_info = parse_country(c2)

    print(f"{'Feature':<15} {c1_info['official_name']:<40} {c2_info['official_name']:40}")
    print(f"{'Population':<15} {f'{c1_info['population']:,}':<40} {f'{c2_info['population']:,}':<40}")
    area1 = f"{c1_info['area']:,} km²" if c1_info['area'] else "Unknown"
    area2 = f"{c2_info['area']:,} km²" if c2_info['area'] else "Unknown"
    print(f"{'Area':<15} {area1:<40} {area2:<40}")
    print(f"{'Region':<15} {c1_info['region']:<40} {c2_info['region']:<40}")
    print(f"{'Capital':<15} {c1_info['capital']:<40} {c2_info['capital']:<40}")

def random_country_fact():
    regions = ["africa", "americas", "asia", "europe", "oceania"]
    random_region = random.choice(regions)

    url = f"https://restcountries.com/v3.1/region/{random_region}"
    cache_file = "cache_all_countries.json"
    all_countries = None

    if os.path.exists(cache_file):
        print("Fetching data from cache file...")
        with open(cache_file, "r") as f:
            all_countries = json.load(f)
    else:
        print("Fetching data for the first time...")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            all_countries = response.json()

            with open(cache_file, "w") as f:
                json.dump(all_countries, f, indent=4)
        except Exception as e:
            print(f"Error: {e}")
            return
    
    random_country = random.choice(all_countries)
    name = random_country.get("name",{}).get("common")
    flag = random_country.get("flag", "🌐")
    demonym = random_country.get("demonyms", {}).get("eng", {}).get("m", "citizens")
    car_side = random_country.get("car", {}).get("side", "right")
    landlocked = "is completely landlocked" if random_country.get("landlocked") else "has beautiful coastlines"
    facts_pool = [
        f"A citizen from here is officially referred to as a {demonym}.",
        f"Motorists in this nation drive on the {car_side} side of the road.",
        f"It {landlocked}."
    ]

    chosen_fact = random.choice(facts_pool)
    print(f"\n RANDOM FACT FOR {name.upper()} {flag}")
    print(f"{chosen_fact}")


def load_saved(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    else:
        return []

def save_country(filename, name):
    saved_countries = load_saved(filename)
    bookmarks = [c.lower().strip() for c in saved_countries]
    if name.lower().strip() not in bookmarks:
        saved_countries.append(name)
        with open(filename, "w") as f:
            json.dump(saved_countries, f, indent=4)

def display_saved(filename):
    bookmarks = load_saved(filename)
    if not bookmarks:
        print("You haven't saved any countries yet!")
        return
    for i, name in enumerate(bookmarks):
        print(f"{i+1}. {name}")


def main():
    while True:
        print("="*40)
        print("      COUNTRY EXPLORER")
        print("="*40)
        print("1. Search country")
        print("2. Explore region")
        print("3. Compare two countries")
        print("4. Random country fact")
        print("5. Saved countries")
        print("6. Quit")

        choice = input("Enter your choice: ").strip()
        print()
        if choice == "6":
            print("Goodbye!")
            break
        elif choice == "1":
            country_name = input("Enter country name: ").strip()
            raw_data = search_country(country_name)
            if raw_data:
                clean_data = parse_country(raw_data)
                display_country(clean_data)

                save_choice = input("Would you like to bookmark this country?(y/n): ").strip().lower()
                if save_choice == "y":
                    save_country("saved_countries.json", clean_data["official_name"])

        elif choice == "2":
            region = input("Enter region: ").strip()
            display_stats(region)

        elif choice == "3":
            country1 = input("Enter the first country: ").strip()
            country2 = input("Enter second country: ").strip()
            compare_countries(country1, country2)

        elif choice == "4":
            random_country_fact()

        elif choice == "5":
            display_saved("saved_countries.json")
        else:
            print("Invalid choice!")
            continue

if __name__ == "__main__":
    main()