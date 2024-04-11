import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
from video_lib import videos

# Load the API key from the .env file
load_dotenv()
key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=key)

def parse_recommendation(recommendation, videos):
    # Split the recommendation into individual titles
    recommended_titles = recommendation.split(", ")
    recommended_videos_info = []

    # Match titles from recommendation to titles and scripts in videos dictionary
    for video_id, video_info in videos.items():
        if video_info["title"] in recommended_titles:
            recommended_videos_info.append((video_info["title"], video_info["script"]))
    
    return recommended_videos_info

def recommend_video(question, videos):
    # Construct a list of video titles for the query
    video_titles = ", ".join([video["title"] for video in videos.values()])
    
    # Send the query to the OpenAI API
    response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant skilled in video recommendation. Select from the provided video list to recommend the most relevant title(s) based on a user's query. RETURN YOUR ANSWER USING ONLY THE VIDEO TITLE(S) FROM THE PROVIDED LIST, IN CSV FORMAT. INCLUDE AT LEAST ONE TITLE, SEPARATING MULTIPLE TITLES WITH COMMAS IF APPLICABLE. DO NOT ADD ANY TEXT BEYOND THE VIDEO TITLE(S). Please try to return more than one video if possible."},
            {"role": "user", "content": f"{question} Available titles: {video_titles}"},
        ])
    
    # Assuming the response is the CSV string of titles
    recommendation = response.choices[0].message.content
    print(recommendation)  # For debugging
    return recommendation

st.title('Video Recommendation System')

user_question = st.text_input("Please enter your question:")
submit_button = st.button('Search')

if submit_button and user_question:
    recommendation = recommend_video(user_question, videos)
    recommended_videos_info = parse_recommendation(recommendation, videos)

    if recommended_videos_info:
        for title, script in recommended_videos_info:
            st.write(f"Recommended Video: {title}")
            st.write(f"Description: {script}")
            st.write("-------")  # Separator for readability
    else:
        st.write("No recommended videos found.")