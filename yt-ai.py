import streamlit as st

from yt_ai.patch_sqlite import patch_sqlite
patch_sqlite()

from yt_ai.crew import YtAi
import yt_dlp

def get_video_info(youtube_url):
    """Get video title and creator using yt-dlp"""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        return {
            'title': info.get('title', 'Unknown Title'),
            'channel': info.get('uploader', 'Unknown Creator')
        }

st.title("📺 YT-AI")

youtube_link = st.text_input("Enter YouTube Video URL:")

if st.button("Get Summary"):
    if youtube_link:
        processing_placeholder = st.empty()
        processing_placeholder.info("⏳ Processing... Please wait.")

        try:
            video_info = get_video_info(youtube_link)
            st.subheader("📽️ Video Details")
            st.markdown(f"""
            <div style="padding: 15px; border-radius: 8px; background-color: #e6e9ef; margin-bottom: 20px;">
                <h3 style="margin-top: 0; color: #1e1e1e;">{video_info['title']}</h3>
                <p style="font-size: 16px; color: #333;"><strong>Creator:</strong> {video_info['channel']}</p>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"Could not fetch video details: {str(e)}")

        inputs = {"youtube_link": youtube_link}
        try:
            result = YtAi().crew().kickoff(inputs=inputs)
            
            summary_text = None
            
            if isinstance(result, dict) and "tasks_output" in result:
                if len(result["tasks_output"]) > 1 and "raw" in result["tasks_output"][1]:
                    summary_text = result["tasks_output"][1]["raw"]
            
            if not summary_text and isinstance(result, dict) and "raw" in result:
                summary_text = result["raw"]
                
            if not summary_text:
                summary_text = str(result)

            processing_placeholder.empty()

            st.subheader("📜 Video Summary")
            st.markdown(f"""
            <div style="font-size: 18px; padding: 20px; border-radius: 10px; border-left: 10px solid #4CAF50; 
                 line-height: 1.8;">
                {summary_text}
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:

            processing_placeholder.empty()
            
            st.error(f"Error: {str(e)}")
            
            st.warning("""
            ### Network Issue? Try using a VPN
            
            YouTube may be blocking requests from your current network. If you're experiencing issues like I did many times, 
            
            1. Try connecting through a VPN
            2. Use a different network connection
            3. Try again in a few minutes
            
            This solves issues related to rate limiting and IP blocking by YouTube.
            """)
    else:
        st.warning("⚠️ Please enter a valid YouTube URL.")