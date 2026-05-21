import requests

def fetch_country(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 404:
            print(f"Country {country_name} not found.")
            return   
        response.raise_for_status()
        return response.json()[0]
    
    except requests.exceptions.ConnectionError:
        print("Connection error. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("The server took too long to respond. Try again later.")
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
    # country_info["area"] = f"{area:.2f} km²" if area else "Unknown"

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


def search_loop():
    while True:
        country_name = input("Enter country: ")
        data = fetch_country(country_name)
        if data is None:
            return
        
        country_dict = parse_country(data)
        display_country(country_dict)
        print()
        choice = input("Do you want to continue?(y/n): ")
        if choice != "y":
            print("Goodbye!")
            break


def main():
    search_loop()

if __name__ == "__main__":
    main()
