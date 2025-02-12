from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

class ChordifyScraper:
    def __init__(self):
        # Configure Selenium Chrome driver
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run without UI
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

        # Initialize WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def get_chords(self, song_url):
        """Extracts chords dynamically from Chordify."""
        self.driver.get(song_url)
        time.sleep(5)  # Wait for JavaScript to load

        try:
            # Find chord elements (update selector if necessary)
            chord_elements = self.driver.find_elements(By.CLASS_NAME, "chord-symbol")

            if not chord_elements:
                return {"error": "No chords found."}

            chords = [chord.text for chord in chord_elements]
            return {"chords": chords}
        except Exception as e:
            return {"error": f"Failed to extract chords. Error: {str(e)}"}

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    scraper = ChordifyScraper()
    
    # ✅ Chordify Song URL
    song_url = "https://chordify.net/chords/ed-sheeran-songs/perfect-chords"

    result = scraper.get_chords(song_url)

    # Save to JSON file
    with open("perfect_chords.json", "w") as f:
        json.dump(result, f, indent=4)

    scraper.close()
    print("✅ Chords Saved to perfect_chords.json")
