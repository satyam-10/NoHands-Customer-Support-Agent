from langchain_core.tools import tool
from app.db.chinook import db
import ast

@tool
def get_albums_by_artist(artist: str):
    """Get all albums by a specific artist.
    
    Search for albums in the music database by artist name.
    Supports partial name matching.
    
    Args:
        artist: The name of the artist to search for
    """
    return db.run(f"""
    SELECT Album.Title, Artist.Name
    FROM Album
    JOIN Artist ON Album.ArtistId = Artist.ArtistId
    WHERE Artist.Name LIKE '%{artist}%';
    """, include_columns=True)

@tool
def check_for_songs(song_title: str):
    """Check if a song exists in the music database.
    
    Search for tracks by song title. Supports partial title matching.
    
    Args:
        song_title: The title of the song to search for
    """
    return db.run(f"""
    SELECT * FROM Track WHERE Name LIKE '%{song_title}%';
    """, include_columns=True)

music_tools = [get_albums_by_artist, check_for_songs]