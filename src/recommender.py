import csv


def load_songs(csv_path):
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)

    return songs


def score_song(user_prefs, song):
    score = 0.0
    reasons = []

    # genre match
    if song["genre"].lower() == user_prefs["favorite_genre"].lower():
        score += 1.0
        reasons.append("genre match (+1.0)")

    # mood match
    if song["mood"].lower() == user_prefs["favorite_mood"].lower():
        score += 1.5
        reasons.append("mood match (+1.5)")

    # energy similarity
    energy_gap = abs(song["energy"] - user_prefs["target_energy"])
    energy_points = max(0, 4.0 - (energy_gap * 8))
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    # tempo similarity
    tempo_gap = abs(song["tempo_bpm"] - user_prefs["target_tempo_bpm"])
    tempo_points = max(0, 1.5 - (tempo_gap / 40))
    score += tempo_points
    reasons.append(f"tempo similarity (+{tempo_points:.2f})")

    # valence similarity
    valence_gap = abs(song["valence"] - user_prefs["target_valence"])
    valence_points = max(0, 1.5 - (valence_gap * 3))
    score += valence_points
    reasons.append(f"valence similarity (+{valence_points:.2f})")

    # danceability similarity
    dance_gap = abs(song["danceability"] - user_prefs["target_danceability"])
    dance_points = max(0, 1.0 - (dance_gap * 2))
    score += dance_points
    reasons.append(f"danceability similarity (+{dance_points:.2f})")

    # acousticness similarity
    acoustic_gap = abs(song["acousticness"] - user_prefs["target_acousticness"])
    acoustic_points = max(0, 1.0 - (acoustic_gap * 2))
    score += acoustic_points
    reasons.append(f"acousticness similarity (+{acoustic_points:.2f})")

    return score, reasons


def recommend_songs(user_prefs, songs, k=5):
    ranked = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)

        ranked.append({
            "title": song["title"],
            "artist": song["artist"],
            "genre": song["genre"],
            "mood": song["mood"],
            "score": score,
            "reasons": reasons
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked[:k]
