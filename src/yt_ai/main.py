import sys
import warnings
from yt_ai.patch_sqlite import patch_sqlite

patch_sqlite()

from yt_ai.crew import YtAi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """Run the crew."""
    youtube_link = input("Enter YouTube video URL: ")
    inputs = {"youtube_link": youtube_link}
    result = YtAi().crew().kickoff(inputs=inputs)
    print("\n📌 **Video Summary:**\n")
    print(result)

if __name__ == "__main__":
    run()
