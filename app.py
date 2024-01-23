import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "4eb4a85a1e114984a80e20c96948cb20"
CLIENT_SECRET = "732026398ebf40f986902e4c998ac24d"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"
    
def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    recommended_music_artist = []
    for i in distances[1:6]:
        # fetch the movie poster
        artist = music.iloc[i[0]].artist
        print(artist)
        print(music.iloc[i[0]].song)
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_names.append(music.iloc[i[0]].song)
        recommended_music_artist.append(music.iloc[i[0]].artist)
    return recommended_music_names,recommended_music_posters,recommended_music_artist

st.header('Autumn Music Recommendation')
music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

music_list = music['song'].values
selected_music = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)
index = music[music['song'] == selected_music].index[0]
data = music.iloc[index]
artist = data[0]
st.write('Artist:',artist)

if st.button('Show Recommendation'):
    recommended_music_names,recommended_music_posters,recommended_music_artist = recommend(selected_music)
    st.subheader("Recommended Songs")
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        
        st.image(recommended_music_posters[0])
        st.caption(recommended_music_names[0])
        st.caption(recommended_music_artist[0])
    with col2:
        
        st.image(recommended_music_posters[1])
        st.caption(recommended_music_names[1])
        st.caption(recommended_music_artist[1])
    with col3:
        
        st.image(recommended_music_posters[2])
        st.caption(recommended_music_names[2])
        st.caption(recommended_music_artist[2])
    with col4:
        
        st.image(recommended_music_posters[3])
        st.caption(recommended_music_names[3])
        st.caption(recommended_music_artist[3])
    with col5:
        
        st.image(recommended_music_posters[4])
        st.caption(recommended_music_names[4])
        st.caption(recommended_music_artist[4])