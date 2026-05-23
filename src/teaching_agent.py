import os
from typing import Any, Dict, List

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()


class InstructorConversationChain:
    """Conversation chain that drives the instructor agent."""

    def __init__(self, prompt_template: PromptTemplate, llm: ChatGroq):
        self.prompt_template = prompt_template
        self.llm = llm

    @classmethod
    def from_llm(cls, llm: ChatGroq) -> "InstructorConversationChain":
        instructor_prompt = """
        You are an instructor teaching the user based on a provided syllabus.
        Review the syllabus and follow it topic-by-topic in order.
        Do not skip or reorder topics.
        Go deep into definitions, formulas (if applicable), and examples for each topic.
        Maintain a supportive and clear teaching style.
        Only teach one stage at a time.
        End each response with '<END_OF_TURN>' to give the user a chance to respond.
        Make sure the user understands before moving on.

        Following '===' is the syllabus about {topic}.
        ===
        {syllabus}
        ===

        Following '===' is the conversation history so far.
        ===
        {conversation_history}
        ===
        """
        prompt = PromptTemplate(
            template=instructor_prompt,
            input_variables=["syllabus", "topic", "conversation_history"],
        )
        return cls(prompt_template=prompt, llm=llm)

    def run(self, **kwargs) -> str:
        formatted = self.prompt_template.format(**kwargs)
        try:
            response = self.llm.invoke([SystemMessage(content=formatted)])
            return response.content if hasattr(response, "content") else str(response)
        except Exception as e:
            return f"⚠️ Instructor error: {str(e)}. Please try again."


class TeachingGPT(BaseModel):
    """Controller for the Teaching Agent."""

    class Config:
        arbitrary_types_allowed = True

    syllabus: str = ""
    conversation_topic: str = ""
    conversation_history: List[str] = []
    teaching_conversation_utterance_chain: InstructorConversationChain = Field(...)

    def seed_agent(self, syllabus: str, task: str):
        self.syllabus = syllabus
        self.conversation_topic = task
        self.conversation_history = []

    def human_step(self, human_input: str):
        self.conversation_history.append(human_input + "<END_OF_TURN>")

    def instructor_step(self) -> str:
        return self._call_instructor()

    def _call_instructor(self) -> str:
        ai_message = self.teaching_conversation_utterance_chain.run(
            syllabus=self.syllabus,
            topic=self.conversation_topic,
            conversation_history="\n".join(self.conversation_history),
        )
        self.conversation_history.append(ai_message)
        return ai_message

    @classmethod
    def from_llm(cls, llm: ChatGroq, **kwargs) -> "TeachingGPT":
        chain = InstructorConversationChain.from_llm(llm)
        return cls(teaching_conversation_utterance_chain=chain, **kwargs)


# Instantiate the global teaching agent
teaching_agent = TeachingGPT.from_llm(
    llm=ChatGroq(temperature=0.9, model_name="llama-3.3-70b-versatile"),
    conversation_history=[],
    syllabus="",
    conversation_topic="",
)
