API_KEY = "UNDISCLOSED"

def get_latitude(location: str):
    r = requests.request("GET", f"https://maps.google.com/maps/api/geocode/json?address={location}&key={API_KEY}")
    r = r.json()
    return r["results"][0]["geometry"]["location"]["lat"]

all_latitudes = []
    for x in tqdm(dataset["origin"]):
        if x != "Not disclosed":
            try:
                res = get_latitude(x)
                print(f"{x:20} : {res}")
            except Exception:
                res = None
        else:
            res = None
        all_latitudes.append(res)
        
print(all_latitudes)
