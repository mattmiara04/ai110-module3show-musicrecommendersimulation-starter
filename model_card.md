# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

SuperSickMusicFinder9000

---

## 2. Intended Use  

This recommender system suggests 3 to 5 songs from a small dataset based on a user's preferred genre, mood, and audio features like energy and tempo. It assumes the user has a single dominant taste profile and is looking for songs that match a specific vibe. This system is built for classroom exploration and demonstration purposes, not for real-world use.
---

## 3. How the Model Works  

The model compares each song in the dataset to a user profile. It gives points when the song’s genre and mood match the user’s preferences. It also calculates similarity scores based on numerical features such as energy, tempo, valence, danceability, and acousticness. The closer a song’s values are to the user’s target values, the more points it receives. After scoring all songs, the system ranks them from highest to lowest and recommends the top results.

I modified the scoring by reducing the weight of genre and increasing the importance of energy similarity. This made the system focus more on the overall vibe instead of just matching labels.

---

## 4. Data  

The dataset contains around 20 songs with features such as genre, mood, energy, tempo, valence, danceability, and acousticness. The songs cover multiple genres including pop, lofi, rock, ambient, jazz, synthwave, indie pop, and EDM. I added additional songs beyond the starter dataset to increase variety. However, the dataset is still small and does not fully represent the diversity of real music tastes.

---

## 5. Strengths  

The system works well when the user profile is clearly defined, such as Happy Pop or Chill Lofi. It produces recommendations that feel reasonable and consistent with the intended vibe. A key strength is transparency, since the scoring process clearly shows why each song was recommended. 

---

## 6. Limitations and Bias 

The system has several limitations. It only uses a small dataset, so recommendations are limited. It also ignores important aspects of music like lyrics, artist popularity, and cultural context. The scoring system can introduce bias depending on how weights are set, which may cause the model to favor certain genres or high-energy songs. It also assumes users have a fixed taste, which is not realistic.
---

## 7. Evaluation  

I tested the recommender using three different user profiles: Happy Pop, Chill Lofi, and Intense Rock. I checked whether the top results matched what I would expect for each profile. I also changed the scoring weights to see how the recommendations shifted. I noticed that increasing the importance of energy caused songs with similar vibes to rank higher, even if they were from different genres.
---

## 8. Future Work  
If I had more time, I would expand the dataset significantly to include more songs and genres. I would also allow users to have multiple preferences instead of a single profile. Another improvement would be adding diversity so that recommendations are not all extremely similar.
---

## 9. Personal Reflection  

This project showed me how recommendation systems work at a basic level by turning user preferences into scores. I learned that even simple models can produce realistic results if the right features are used. It also made me realize how easy it is for bias to enter the system through data or scoring choices, which can affect what users are recommended.
