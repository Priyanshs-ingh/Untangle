import json
from scrape_chords import UltimateGuitarScraper  # Import the scraper

class GuitarTeacher:
    def __init__(self):
        self.scraper = UltimateGuitarScraper()

    def teach_song(self, song_name):
        """Fetch chords using the scraper and return song details."""
        return self.scraper.fetch_song_chords(song_name)

if __name__ == "__main__":
    teacher = GuitarTeacher()
    song = teacher.teach_song("Madari")
    print(f"🎸 Song: {song['song']}")
    print(f"🎵 Chords: {', '.join(song['chords'])}")
