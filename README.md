# YTai - YouTube Video Transcript and Summary Tool

YTai is an AI-powered tool that extracts transcripts from YouTube and generates summaries using crewAI. 
## Features

- Automatic extraction of transcripts from YouTube videos
- AI-powered summarization of video content
- Sequential multi-agent workflow using crewAI

## Prerequisites

- Python >=3.10 <=3.13
- [UV package manager] or pip

## Installation

1. Clone the repository, 
    
2. Install dependencies using UV:
    
    pip install uv
    
    uv pip install -r requirements.txt
    
    Or, use pip:
    
    pip install -r requirements.txt
    
3. Set up your environment variables by creating a [.env] file in the project root:
    
    MODEL=<your-chosen-llm-model>
    
    GROQ_API_KEY=<your-groq-api-key>
    
    You can use other LLM providers by adding the appropriate API keys (e.g., `OPENAI_API_KEY`).
    

## Usage

Run the tool from the terminal

python -m src.yt_ai.main

Or if you've installed the package:

yt_ai

When prompted, enter a YouTube video URL. The tool will:

1. Extract the transcript from the video
2. Generate a concise summary
3. Display the summary in the console

