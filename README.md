# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders


This project builds a small music recommender system that suggests songs from a CSV catalog based on a user's taste profile. My version uses song features such as genre, mood, energy, tempo, valence, danceability, and acousticness to compare each song against a target listener profile. The system then scores every song, ranks them from best match to worst match, and returns the top recommendations. The goal is to show how a simple AI-style recommender can turn structured data into suggestions while still having limits and biases.
---

## How The System Works
Each Song in my system is represented by structured features from the CSV file, including genre, mood, energy, tempo_bpm, valence, danceability, and acousticness. These features describe the overall vibe of a track in a simplified way.

The UserProfile stores the listener's target preferences, such as a favorite genre, favorite mood, target energy level, target tempo, target valence, target danceability, and target acousticness. This creates a simple taste profile that the recommender can compare against each song.

The Recommended computes a score for every song by checking whether important category features like genre and mood match the user's preferences, and by measuring how close each numeric feature is to the user's target values. Songs with better matches receive higher scores.

After every song is scored, the system sorts the songs from highest score to lowest score and recommends the top results. This makes the recommender easy to understand because every recommendation comes from a clear scoring rule rather than a hidden black-box model.

---

My scoring design gives the most importance to genre and overall vibe. Genre match has the highest fixed bonus, followed by mood match. Numeric features such as energy, tempo, valence, danceability, and acousticness use similarity scoring, which means a song gets more points when it is closer to the user's target values. After every song is scored, the recommender sorts the songs by total score and returns the strongest matches.

---
## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

I tested the recommender with three different user profiles: Happy Pop, Chill Lofi, and Intense Rock. In the original version, genre had a strong influence on the final ranking, which often pushed songs from the favorite genre to the top even when other features were only a moderate match.

I then ran a weight-shift experiment by reducing the genre bonus and increasing the importance of energy similarity. After this change, the recommendations became more sensitive to the user’s target vibe instead of relying as heavily on genre labels. Some songs from outside the favorite genre moved higher because their energy matched the profile more closely.

---

## Limitations and Risks

This recommender only works on a very small song catalog, so its recommendations are limited by the size and variety of the dataset. It also depends entirely on the selected features, which means it cannot understand lyrics, personal memories, cultural context, or changing taste over time. Another limitation is that hand-chosen weights can over-favor certain features, such as genre or energy, which may make the system feel biased toward one type of song.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

This project helped me understand how recommendation systems turn user preferences and item features into a ranked prediction. Even though this system is simple, it still demonstrates the core idea behind real recommenders where it represents data, compares it, and assigns scores. I learned that the features you choose, like genre, mood, and energy, directly control what the model is capable of recommending.

It also showed me how bias can easily enter a system. A small or unbalanced dataset can limit what gets recommended, and the weights in the scoring system can favor certain types of songs over others. This means the system might repeatedly push similar content, even if the user’s actual taste is more complex. It made me realize that real-world recommenders need to be carefully designed to avoid reinforcing narrow patterns.

---

# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"


