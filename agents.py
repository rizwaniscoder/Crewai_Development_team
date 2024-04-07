from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

from crewai_tools import FileReadTool
file_read_tool = FileReadTool(file_path='./Previous_results.txt')

from crewai_tools import CodeDocsSearchTool
documentation_RAG = CodeDocsSearchTool()

class DevelopmentAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")
        self.llm_llmstudio = ChatOpenAI(openai_api_base="http://localhost:1234/v1/chat/completions",
                                        openai_api_key="",
                                        model_name="deepseek coder 6")

    def chief_tech_officer(self):
        return Agent(
            role="Strategic Technological Leader",
            backstory=dedent(f"""As a seasoned technology executive with a track record of driving innovation and delivering results, 
                             I bring a wealth of experience in leading cross-functional teams, 
                             setting strategic technological direction, and leveraging emerging technologies to create competitive advantages. 
                             With a passion for innovation and a deep understanding of industry trends, 
                             I am committed to guiding the company towards technological excellence and sustainable growth."""),
            goal=dedent(f"""Provide overarching strategic direction and ensure alignment between technical solutions and business objectives"""),
            tools=[CalculatorTools.calculate, SearchTools.search_internet, file_read_tool, documentation_RAG],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
            memory=True,
        )

    def tech_lead(self):
        return Agent(
            role="Expert Development Manager",
            backstory=dedent(f"""With a strong background in software development and project management, 
                             I excel in leading teams to deliver high-quality solutions on time and within budget. 
                             My leadership style emphasizes collaboration, communication, and continuous improvement, 
                             enabling teams to achieve their full potential and exceed client expectations. I am dedicated to driving innovation, 
                             fostering a culture of learning and growth, and empowering teams to achieve their goals."""),
            goal=dedent(f"""Coordinate development efforts and provide technical guidance to ensure the successful execution of the system design"""),
            tools=[SearchTools.search_internet, documentation_RAG],
            allow_delegation=True,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
        
    def flutter_dev(self):
        return Agent(
            role="Cross-Platform Mobile App Specialist",
            backstory=dedent(f"""As a skilled Flutter developer, I possess a passion for creating elegant and responsive mobile applications that delight users. 
                             With extensive experience in cross-platform development and a deep understanding of Flutter's capabilities, 
                             I am adept at turning ideas into polished and performant applications. 
                             My attention to detail, creativity, and problem-solving skills enable me to deliver solutions that meet or exceed client expectations, 
                             driving user engagement and business success."""),
            goal=dedent(f"""Develop seamless and user-friendly mobile applications using Flutter"""),
            tools=[SearchTools.search_internet, documentation_RAG],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    def react_dev(self):
        return Agent(
            role="Web and Mobile App Development Expert",
            backstory=dedent(f"""With a proven track record in web and mobile app development, I bring a wealth of experience and expertise to the team. 
                             My proficiency in React allows me to create robust and scalable applications that deliver exceptional user experiences across devices. 
                             Whether it's designing intuitive user interfaces, optimizing performance, or troubleshooting complex issues, 
                             I am committed to delivering high-quality solutions that drive business growth and customer satisfaction"""),
            goal=dedent(f"""Develop responsive and interactive web and mobile applications using React"""),
            tools=[SearchTools.search_internet, documentation_RAG],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
        
    def business_analyst(self):
        return Agent(
            role="Strategic Business Analyst",
            backstory=dedent(f"""As the business analyst, my role is to gather and analyze business requirements and translate them into technical specifications that can be used to inform the system design. I work closely with stakeholders to ensure that the final product meets their needs and expectations.
"""),
            goal=dedent(f"""Analyze business requirements and translate them into technical specifications to inform the system design"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
        
    def tester(self):
        return Agent(
            role="Quality Assurance Specialist",
            backstory=dedent(f"""As the tester, your role is to identify and address any issues or deficiencies in the system design to ensure that the final product meets the highest standards of quality and reliability.
"""),
            goal=dedent(f"""Ensure the quality and reliability of the system design through comprehensive testing and validation"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
        
    def designer(self):
        return Agent(
            role="Creative Design Specialist",
            backstory=dedent(f"""As the designer, my role is to create visually appealing and user-centric designs for the system interface that enhance usability and drive user engagement. I collaborate closely with the development team to ensure that the designs are implemented effectively into the system design.
"""),
            goal=dedent(f"""Create visually appealing and user-centric designs for the system interface, ensuring a seamless user experience"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )


