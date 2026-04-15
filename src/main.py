from src.recommender import load_songs, recommend_songs


def print_recommendations(name, profile, songs):
    print(f"\n=== {name} ===")

    results = recommend_songs(profile, songs, k=5)

    for i, song in enumerate(results, 1):
        print(f"\n{i}. {song['title']} - {song['artist']}")
        print(f"   Score: {song['score']:.2f}")
        print(f"   Genre: {song['genre']} | Mood: {song['mood']}")
        print("   Reasons:")
        for r in song["reasons"]:
            print(f"   - {r}")


def main():
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    happy_pop = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.85,
        "target_tempo_bpm": 120,
        "target_valence": 0.85,
        "target_danceability": 0.80,
        "target_acousticness": 0.15
    }

    chill_lofi = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.35,
        "target_tempo_bpm": 75,
        "target_valence": 0.60,
        "target_danceability": 0.58,
        "target_acousticness": 0.80
    }

    intense_rock = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.92,
        "target_tempo_bpm": 150,
        "target_valence": 0.50,
        "target_danceability": 0.65,
        "target_acousticness": 0.10
    }

    print_recommendations("Happy Pop", happy_pop, songs)
    print_recommendations("Chill Lofi", chill_lofi, songs)
    print_recommendations("Intense Rock", intense_rock, songs)


if __name__ == "__main__":
    main()