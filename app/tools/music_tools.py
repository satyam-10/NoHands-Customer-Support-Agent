from langchain_core.tools import tool
from app.db.chinook import db
import ast

@tool
def get_albums_by_artist(artist: str):
    return db.run(f"""
    SELECT Album.Title, Artist.Name
    FROM Album
    JOIN Artist ON Album.ArtistId = Artist.ArtistId
    WHERE Artist.Name LIKE '%{artist}%';
    """, include_columns=True)

@tool
def check_for_songs(song_title: str):
    return db.run(f"""
    SELECT * FROM Track WHERE Name LIKE '%{song_title}%';
    """, include_columns=True)

music_tools = [get_albums_by_artist, check_for_songs]
