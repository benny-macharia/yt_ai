from crewai.tools import BaseTool
from youtube_transcript_api import YouTubeTranscriptApi

class YouTubeTranscriptTool(BaseTool):
    name: str = "youtube_transcript_tool"
    description: str = "Fetches the transcript of a YouTube video using its URL."
    
    def _run(self, video_url: str) -> str:
        """Fetches the transcript of a YouTube video using its URL."""
        video_id = video_url.split("v=")[-1]
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            return " ".join([entry["text"] for entry in transcript])
        except Exception as e:
            return f"Error fetching transcript: {str(e)}"

youtube_transcript_tool = YouTubeTranscriptTool()