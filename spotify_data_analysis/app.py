
# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Set the page background to black and text to white using CSS
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #000000;
#         color: #FFFFFF;
#     }
#     h1 {
#         color: #1DB954; /* Spotify green for headings */
#     }
#     h2, h3, h4 {
#         color: #1DB954; /* Spotify green for subheadings */
#     }
#     .stApp {
#         background-color: #000000;
#     }
#     header, .css-1q8dd3e, .css-zbg2yr, .css-1v3fvcr, .css-2ykyy4 { 
#         background-color: #000000; /* Make the top bar black */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Spotify logo and title
# st.image('https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg', width=100)
# st.title("Spotify 2023 Analysis")

# @st.cache_data
# def load_data():
#     df = pd.read_csv('./spotify_data_analysis/spotify-2023.csv', encoding='ISO-8859-1')
#     df['release_date'] = pd.to_datetime(df['released_year'].astype(str) + '-' +
#                                         df['released_month'].astype(str) + '-' +
#                                         df['released_day'].astype(str))
#     df.drop(columns=['released_year', 'released_month', 'released_day', 'bpm', 'key', 'mode'], inplace=True)
#     df = df.drop([574])
#     df['streams'] = pd.to_numeric(df['streams'])
#     df = df.sort_values(by='streams', ascending=False)
#     df = df.drop_duplicates(subset='track_name', keep='first')
#     df['in_deezer_playlists'] = df['in_deezer_playlists'].str.replace(',', '').astype(int)
#     return df

# df = load_data()

# st.write("### Dataset Overview")
# st.dataframe(df, width=1000, height=400)

# # Set the Seaborn theme to dark
# sns.set_theme(style="darkgrid")
# plt.style.use('dark_background')

# st.write("### Top 10 Artists with the Most Streamed Songs in 2023")
# top_artists = df['artist(s)_name'].value_counts().head(10)

# fig, ax = plt.subplots(figsize=(10, 6))
# sns.barplot(x=top_artists.index, y=top_artists.values, ax=ax, palette="viridis")
# ax.set_title('Top 10 Artists with Most Hits in 2023', color='#1DB954')
# ax.set_xlabel('Artist', color='white')
# ax.set_ylabel('Number of Hits', color='white')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
# ax.set_yticklabels(ax.get_yticks(), color='white')
# st.pyplot(fig)

# st.write("### Top 10 Most Streamed Songs in 2023")
# fig, ax = plt.subplots(figsize=(20, 10))
# sns.barplot(x=df['track_name'][:10], y=df['streams'][:10], ax=ax, palette="magma")
# ax.set_title('Top 10 Streamed Songs in 2023', color='#1DB954')
# ax.set_xlabel('Song', color='white')
# ax.set_ylabel('Streams', color='white')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
# ax.set_yticklabels(ax.get_yticks(), color='white')
# st.pyplot(fig)

# st.write("### Relationship Between Number of Artists in a Song and Streams")
# fig, ax = plt.subplots(figsize=(20, 10))
# sns.barplot(x=df['artist_count'], y=df['streams'], ax=ax, palette="plasma")
# ax.set_title('Relationship Between Number of Artists in a Song and Streams', color='#1DB954')
# ax.set_xlabel('Number of Artists', color='white')
# ax.set_ylabel('Streams', color='white')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
# ax.set_yticklabels(ax.get_yticks(), color='white')
# st.pyplot(fig)

# st.write("### Relationship Between Most Streamed Songs and Platforms in 2023")

# st.write("#### Spotify Playlists")
# fig, ax = plt.subplots(figsize=(20, 10))
# sns.regplot(x='streams', y='in_spotify_playlists', data=df, ax=ax, scatter_kws={'color': '#1DB954'}, line_kws={'color': 'white'})
# ax.set_title('Relationship Between Most Streamed Songs and Spotify Playlists in 2023', color='#1DB954')
# ax.set_xlabel('Streams', color='white')
# ax.set_ylabel('Number of Spotify Playlists', color='white')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
# ax.set_yticklabels(ax.get_yticks(), color='white')
# st.pyplot(fig)

# st.write("#### Apple Music Playlists")
# fig, ax = plt.subplots(figsize=(20, 10))
# sns.regplot(x='streams', y='in_apple_playlists', data=df, ax=ax, scatter_kws={'color': '#1DB954'}, line_kws={'color': 'white'})
# ax.set_title('Relationship Between Most Streamed Songs and Apple Playlists in 2023', color='#1DB954')
# ax.set_xlabel('Streams', color='white')
# ax.set_ylabel('Number of Apple Playlists', color='white')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
# ax.set_yticklabels(ax.get_yticks(), color='white')
# st.pyplot(fig)

# st.write("#### Deezer Playlists")
# fig, ax = plt.subplots(figsize=(20, 10))
# sns.regplot(x='streams', y='in_deezer_playlists', data=df, ax=ax, scatter_kws={'color': '#1DB954'}, line_kws={'color': 'white'})
# ax.set_title('Relationship Between Most Streamed Songs and Deezer Playlists in 2023', color='#1DB954')
# ax.set_xlabel('Streams', color='white')
# ax.set_ylabel('Number of Deezer Playlists', color='white')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
# ax.set_yticklabels(ax.get_yticks(), color='white')
# st.pyplot(fig)

# st.write("### Correlation Heatmap of Audio Features")
# fig, ax = plt.subplots(figsize=(12, 8))
# corr = df[['danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%','liveness_%', 'speechiness_%']].corr()
# sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
# ax.set_title('Correlation Heatmap of Audio Features', color='#1DB954')
# st.pyplot(fig)

# # Average Streams by Release Month
# st.write("### Average Streams by Release Month")
# df['release_month'] = df['release_date'].dt.month
# monthly_avg_streams = df.groupby('release_month')['streams'].mean()

# fig, ax = plt.subplots(figsize=(10, 6))
# sns.barplot(x=monthly_avg_streams.index, y=monthly_avg_streams.values, ax=ax, palette='viridis')
# ax.set_title('Average Streams by Release Month', color='#1DB954')
# ax.set_xlabel('Month', color='white')
# ax.set_ylabel('Average Streams', color='white')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
# ax.set_yticklabels(ax.get_yticks(), color='white')
# st.pyplot(fig)

# # Streams vs. Release Date
# st.write("### Streams VS Release Date")
# fig, ax = plt.subplots(figsize=(12, 8))
# sns.scatterplot(x='release_date', y='streams', data=df, hue='artist_count', palette='deep', ax=ax)
# ax.set_title('Streams vs. Release Date', color='#1DB954')
# ax.set_xlabel('Release Date', color='white')
# ax.set_ylabel('Streams', color='white')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
# ax.set_yticklabels(ax.get_yticks(), color='white')
# st.pyplot(fig)

# # Correlation Between Audio Features and Streams
# st.write("### Correlation Between Audio Features and Streams")
# fig, ax = plt.subplots(figsize=(12, 8))
# audio_corr = df[['streams', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 
#                  'instrumentalness_%', 'liveness_%', 'speechiness_%']].corr()
# sns.heatmap(audio_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
# ax.set_title('Correlation Between Audio Features and Streams', color='#1DB954')
# st.pyplot(fig)



import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the page background to black and text to white using CSS
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #FFFFFF;
    }
    h1 {
        color: #1DB954; /* Spotify green for headings */
    }
    h2, h3, h4 {
        color: #1DB954; /* Spotify green for subheadings */
    }
    .stApp {
        background-color: #000000;
    }
    header, .css-1q8dd3e, .css-zbg2yr, .css-1v3fvcr, .css-2ykyy4 { 
        background-color: #000000; /* Make the top bar black */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Spotify logo and title
st.image('https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg', width=100)
st.title("Spotify 2023 Analysis")

@st.cache_data
def load_data():
    df = pd.read_csv('./spotify-2023.csv', encoding='ISO-8859-1')
    df['release_date'] = pd.to_datetime(df['released_year'].astype(str) + '-' +
                                        df['released_month'].astype(str) + '-' +
                                        df['released_day'].astype(str))
    df.drop(columns=['released_year', 'released_month', 'released_day', 'bpm', 'key', 'mode'], inplace=True)
    df = df.drop([574])
    df['streams'] = pd.to_numeric(df['streams'])
    df = df.sort_values(by='streams', ascending=False)
    df = df.drop_duplicates(subset='track_name', keep='first')
    df['in_deezer_playlists'] = df['in_deezer_playlists'].str.replace(',', '').astype(int)
    return df

df = load_data()

st.write("### Dataset Overview")
st.dataframe(df, width=1000, height=400)


# Set the Seaborn theme to dark
sns.set_theme(style="darkgrid")
plt.style.use('dark_background')

st.write("### Top 10 Artists with the Most Streamed Songs in 2023")
top_artists = df['artist(s)_name'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_artists.index, y=top_artists.values, ax=ax, palette="viridis")
ax.set_title('Top 10 Artists with Most Hits in 2023', color='#1DB954')
ax.set_xlabel('Artist', color='white')
ax.set_ylabel('Number of Hits', color='white')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
ax.set_yticklabels(ax.get_yticks(), color='white')
st.pyplot(fig)

st.write("### Top 10 Most Streamed Songs in 2023")
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(x=df['track_name'][:10], y=df['streams'][:10], ax=ax, palette="magma")
ax.set_title('Top 10 Streamed Songs in 2023', color='#1DB954')
ax.set_xlabel('Song', color='white')
ax.set_ylabel('Streams', color='white')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
ax.set_yticklabels(ax.get_yticks(), color='white')
st.pyplot(fig)

st.write("### Relationship Between Number of Artists in a Song and Streams")
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(x=df['artist_count'], y=df['streams'], ax=ax, palette="plasma")
ax.set_title('Relationship Between Number of Artists in a Song and Streams', color='#1DB954')
ax.set_xlabel('Number of Artists', color='white')
ax.set_ylabel('Streams', color='white')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
ax.set_yticklabels(ax.get_yticks(), color='white')
st.pyplot(fig)

st.write("### Relationship Between Most Streamed Songs and Platforms in 2023")

st.write("#### Spotify Playlists")
fig, ax = plt.subplots(figsize=(20, 10))
sns.regplot(x='streams', y='in_spotify_playlists', data=df, ax=ax, scatter_kws={'color': '#1DB954'}, line_kws={'color': 'white'})
ax.set_title('Relationship Between Most Streamed Songs and Spotify Playlists in 2023', color='#1DB954')
ax.set_xlabel('Streams', color='white')
ax.set_ylabel('Number of Spotify Playlists', color='white')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
ax.set_yticklabels(ax.get_yticks(), color='white')
st.pyplot(fig)

st.write("#### Apple Music Playlists")
fig, ax = plt.subplots(figsize=(20, 10))
sns.regplot(x='streams', y='in_apple_playlists', data=df, ax=ax, scatter_kws={'color': '#1DB954'}, line_kws={'color': 'white'})
ax.set_title('Relationship Between Most Streamed Songs and Apple Playlists in 2023', color='#1DB954')
ax.set_xlabel('Streams', color='white')
ax.set_ylabel('Number of Apple Playlists', color='white')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
ax.set_yticklabels(ax.get_yticks(), color='white')
st.pyplot(fig)

st.write("#### Deezer Playlists")
fig, ax = plt.subplots(figsize=(20, 10))
sns.regplot(x='streams', y='in_deezer_playlists', data=df, ax=ax, scatter_kws={'color': '#1DB954'}, line_kws={'color': 'white'})
ax.set_title('Relationship Between Most Streamed Songs and Deezer Playlists in 2023', color='#1DB954')
ax.set_xlabel('Streams', color='white')
ax.set_ylabel('Number of Deezer Playlists', color='white')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
ax.set_yticklabels(ax.get_yticks(), color='white')
st.pyplot(fig)

st.write("### Correlation Heatmap of Audio Features")
fig, ax = plt.subplots(figsize=(12, 8))
corr = df[['danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%','liveness_%', 'speechiness_%']].corr()
sns.heatmap(corr, annot=True, cmap=sns.light_palette("#1DB954", as_cmap=True), vmin=-1, vmax=1, ax=ax)
ax.set_title('Correlation Heatmap of Audio Features', color='#1DB954')
st.pyplot(fig)

# Average Streams by Release Month
st.write("### Average Streams by Release Month")
df['release_month'] = df['release_date'].dt.month
monthly_avg_streams = df.groupby('release_month')['streams'].mean()

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=monthly_avg_streams.index, y=monthly_avg_streams.values, ax=ax, palette='viridis')
ax.set_title('Average Streams by Release Month', color='#1DB954')
ax.set_xlabel('Month', color='white')
ax.set_ylabel('Average Streams', color='white')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
ax.set_yticklabels(ax.get_yticks(), color='white')
st.pyplot(fig)

# Streams vs. Release Date
st.write("### Streams VS Release Date")
fig, ax = plt.subplots(figsize=(12, 8))
sns.scatterplot(x='release_date', y='streams', data=df, hue='artist_count', palette='deep', ax=ax)
ax.set_title('Streams vs. Release Date', color='#1DB954')
ax.set_xlabel('Release Date', color='white')
ax.set_ylabel('Streams', color='white')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
ax.set_yticklabels(ax.get_yticks(), color='white')
st.pyplot(fig)

# Correlation Between Audio Features and Streams
st.write("### Correlation Between Audio Features and Streams")
fig, ax = plt.subplots(figsize=(12, 8))
audio_corr = df[['streams', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 
                 'instrumentalness_%', 'liveness_%', 'speechiness_%']].corr()
sns.heatmap(audio_corr, annot=True, cmap=sns.light_palette("#1DB954", as_cmap=True), vmin=-1, vmax=1, ax=ax)
ax.set_title('Correlation Between Audio Features and Streams', color='#1DB954')
st.pyplot(fig)
