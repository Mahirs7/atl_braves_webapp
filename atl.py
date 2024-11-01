import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('BattedBallData.xlsx')

st.title("Baseball Data Visualization")

st.header("Dataset Preview")
st.write("Here's a quick look at the dataset:")
st.write(data.head())

st.sidebar.header("Filter Data")
player = st.sidebar.selectbox("Select Player", data['BATTER'].unique())
filtered_data = data[data['BATTER'] == player]

st.header(f"Data for {player}")
st.write(filtered_data)

st.header("Launch Angle vs Exit Speed")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=filtered_data, x='LAUNCH_ANGLE', y='EXIT_SPEED', hue='PLAY_OUTCOME')
plt.xlabel("Launch Angle (degrees)")
plt.ylabel("Exit Speed (mph)")
plt.title("Launch Angle vs Exit Speed by Play Outcome")
st.pyplot(plt)

st.header("Hit Distance vs Hang Time")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=filtered_data, x='HIT_DISTANCE', y='HANG_TIME', hue='PLAY_OUTCOME')
plt.xlabel("Hit Distance (feet)")
plt.ylabel("Hang Time (seconds)")
plt.title("Hit Distance vs Hang Time by Play Outcome")
st.pyplot(plt)

st.header("Distribution of Exit Speed")
plt.figure(figsize=(10, 6))
sns.histplot(filtered_data['EXIT_SPEED'], bins=20, kde=True)
plt.xlabel("Exit Speed (mph)")
plt.title("Distribution of Exit Speed")
st.pyplot(plt)

st.header("Distribution of Launch Angle")
plt.figure(figsize=(10, 6))
sns.histplot(filtered_data['LAUNCH_ANGLE'], bins=20, kde=True)
plt.xlabel("Launch Angle (degrees)")
plt.title("Distribution of Launch Angle")
st.pyplot(plt)


st.header("Play Outcomes")
outcome_counts = filtered_data['PLAY_OUTCOME'].value_counts()
st.write("Number of Each Play Outcome for the Selected Player")
st.write(outcome_counts)

st.header("Play Videos")
st.write("Click on the links below to view videos of each play.")
for i, row in filtered_data.iterrows():
    st.write(f"{row['PLAY_OUTCOME']} - [Watch Video]({row['VIDEO_LINK']})")

st.sidebar.header("About")
st.sidebar.info("This application visualizes baseball data, allowing users to explore different metrics like exit speed, launch angle, and play outcomes.")

# Run command for reference
# st.sidebar.write("To run this app, use the command: `streamlit run app.py`")
