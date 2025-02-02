

def parse_property_data(pd):
    address = pd.get("address", {})
    full_address = f"{address.get('streetAddress', '')}, {address.get('city', '')}, {address.get('state', '')}, {address.get('zipcode', '')} {address.get('neighborhood', '')}".strip()

    data = {
        "buildingName": pd.get("buildingName", ""),
        "streetAddress": pd.get("streetAddress", ""),
        "latitude": pd.get("latitude", ""),
        "longitude": pd.get("longitude", ""),
        "fullAddress": pd.get("fullAddress", full_address),
        "isWaitlisted": "Yes" if pd.get("isWaitlisted") else "No",
        "contactType": "For Rent" if pd.get("contactType") == "FOR_RENT" else "None",
        "hasPetPark": "Yes" if pd.get("hasPetPark") else "No",
        "hasHotTub": "Yes" if pd.get("hasHotTub") else "No",
        "hasSauna": "Yes" if pd.get("hasSauna") else "No",
        "hasSwimmingPool": "Yes" if pd.get("hasSwimmingPool") else "No",
        "hasAssistedLiving": "Yes" if pd.get("hasAssistedLiving") else "No",
        "hasSharedLaundry": "Yes" if pd.get("hasSharedLaundry") else "No",
        "hasElevator": "Yes" if pd.get("hasElevator") else "No",
        "currency": pd.get("currency", "USD"),
        "buildingPhoneNumber": pd.get("buildingPhoneNumbr", ""),
        "county": pd.get("county", ""),
        "homeTypes": pd.get("homeTypes", [""])[0],
        "specialOffers": "Yes" if pd.get("specialOffers", "No") else "No" ,
        "description": pd.get("description", "")
    }

    gallery_photos = []
    for item in pd.get("galleryPhotos", []):
        webp_sources = item.get("mixedSources", {}).get("webp", [])
        if webp_sources:
            gallery_photos.append(webp_sources[-1].get("url", ""))
    data["galleryPhotos"] = gallery_photos

    return data