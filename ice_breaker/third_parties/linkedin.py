import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/anudeepsingapore/07b01f6abbaa0cf3cd064eb36b1b5f55/raw/7083345f387b6e942855ce8cb646e425ef684c83/anudeep-bio.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )

    data = response.json()
    data = {
        k: v
        for k,v in data.items()
        if v not in([], "", "", None)
    }
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://gist.githubusercontent.com/anudeepsingapore/07b01f6abbaa0cf3cd064eb36b1b5f55/raw/7083345f387b6e942855ce8cb646e425ef684c83/anudeep-bio.json",
            mock=True
        )
    )
        
    