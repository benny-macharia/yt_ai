from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from yt_ai.tools.youtube_transcript_tool import youtube_transcript_tool

@CrewBase
class YtAi():
    """YtAi crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    tool_functions = {
        'youtube_transcript_tool': youtube_transcript_tool
    }

    @agent
    def transcriber(self) -> Agent:
        return Agent(
            config=self.agents_config['transcriber'],
            tools=[youtube_transcript_tool],
            verbose=True
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            verbose=True
        )

    @task
    def extract_transcript_task(self) -> Task:
        return Task(
            config=self.tasks_config['extract_transcript_task'],
            tools=[youtube_transcript_tool]
        )

    @task
    def summarize_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarize_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the YtAi crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )