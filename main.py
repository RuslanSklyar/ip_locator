import requests
import folium


def main():
    try:
        response = requests.get(url=f'http://ip-api.com/json/').json()

        data = {
            "[IP]": response.get("query"),
            "[Country]": response.get("country"),
            "[City]": response.get("city"),
            "[Region]": response.get("regionName"),
            "[Index]": response.get("zip"),
            "[Internet]": response.get("isp"),
            "[Lat]": response.get("lat"),
            "[Lon]": response.get("lon")
        }

        for k, v in data.items():
            if (k != "[Lat]") and (k != "[Lon]"):
                print(f"{k}: {v}")

        map_info = folium.Map(location=[response.get("lat"), response.get("lon")])
        map_info.save(f'{data["[IP]"]}  {data["[City]"]}.html')

    except requests.exceptions.ConnectionError:
        print("error connect")


if __name__ == "__main__":
    main()
