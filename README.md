# Spotify bot script

The Python library for Spotify's Web API, <i>spotipy</i>, is a bit limited in its features. It lacks the following features for public users:
- Historic data
- Number of plays per song and album
- Statistical breakdown of song and album by region and country
- [Since late 2024, the lack of ability to pull stats from algorithmic and Spotify-owned editorial playlists](https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api)

Sp what does this leave us? Not much, except for a category called <b>popularity</b>. Popularity is score from 0-100 that defines how popular a track is relative to every other song on the platform. This score is especially important to artists because it helps determine if a song is popular enough to appear on Spotify's algorithmically-curated playlists, and consistently being on a playlist rotation is a make-or-break factor for many up-and-coming artists by making them more noticeable to the endless amount of listeners with similar tastes. The popularity score is also a good benchmark to see which songs (and indirectly their relevant genre) have staying power long after they were released.

This bot was made possible thanks to [spotipy](https://spotipy.readthedocs.io/en/2.12.0/).
