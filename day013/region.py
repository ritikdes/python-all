import requests

def get_region_data(region):
    url = f"https://restcountries.com/v3.1/region/{region}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.ConnectionError:
        print("Connection error!")
    except requests.exceptions.Timeout:
        print("The server took too long to respond!")
    except Exception as e:
        print(f"An unexpected error: {e}")
        return None


def get_population_data(countries):
    population_stats = {}
    total_population = 0
    high_population_countries = {}
    most_populous = max(countries, key=lambda x: x.get("population", 0))
    least_populous = min(countries, key=lambda x: x.get("population", 0))
    for c in countries:
        popn = c.get('population', 0)
        total_population += popn
        if popn > 50000000:
            high_population_countries[c.get("name", {}).get("common")] = popn
    
    average_popn = total_population // len(countries) if len(countries) != 0 else 0
    
    population_stats["most_pop_name"] = most_populous.get("name", {}).get("common")
    population_stats["most_pop_val"] = most_populous.get("population", 0)

    population_stats["least_pop_name"] = least_populous.get("name", {}).get("common")
    population_stats["least_pop_val"] = least_populous.get("population", 0)

    population_stats["average_population"] = average_popn
    population_stats["over_50m"] = high_population_countries

    return population_stats


def get_area_stats(countries):
    largest_countries = sorted(countries, key=lambda x: x.get("area", 0), reverse=True)
    return largest_countries


def display_region_report(region):
    countries_list = get_region_data(region)

    if countries_list is None:
        print("Could not fetch the region's data")
        return
    
    stats = get_population_data(countries_list)
    area_list = get_area_stats(countries_list)

    print(f"===== {region.upper()} REGION REPORT =====")
    print("\nPopulation Stats:")
    print(f"Most Populous: {stats['most_pop_name']:<20} | {stats['most_pop_val']:,}")
    print(f"Least Populous: {stats['least_pop_name']:<20} | {stats['least_pop_val']:,}")
    print(f"Average Population: {stats['average_population']:,}")

    print(f"\nContries over 50M population: {len(stats['over_50m'])}")
    for name, pop in stats["over_50m"].items():
        print(f"{name:<20}: {pop:,}")

    print("\nTop 5 Largest by Area:")
    for l in area_list[:5]:
        print(f"{l.get('name',{}).get('common'):<20}: {l.get('area',0):,} km²")


def main():
    region = input("Enter a region: ").lower().strip()

    display_region_report(region)

if __name__ == "__main__":
    main()