import os
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from .tools import check_patient_history, medical_research_tool, insurance_check_tool, emergency_booking_tool

class MedFlowOrchestrator:
    def __init__(self):
        # Configure ChatOpenAI to talk to OpenRouter
        self.llm = ChatOpenAI(
            model=os.getenv("OPENROUTER_MODEL", "openai/gpt-4o"),
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            openai_api_base="https://openrouter.ai/api/v1",
            default_headers={
                "HTTP-Referer": "http://localhost:3000", # Required by OpenRouter
                "X-Title": "MedFlow Agent",             # Optional
            },
            temperature=0
        )

    def _create_specialist(self, name, system_msg, tools):
        prompt = ChatPromptTemplate.from_messages([
            ("system", f"You are the {name}. {system_msg}"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        agent = create_openai_functions_agent(self.llm, tools, prompt)
        return AgentExecutor(agent=agent, tools=tools, verbose=True)

    def run(self, user_input):
        # Define Specialists
        researcher = self._create_specialist("Medical Researcher", "Analyze symptoms based on guidelines.", [medical_research_tool])
        billing = self._create_specialist("Insurance Auditor", "Check coverage for specific plans.", [insurance_check_tool])
        ops = self._create_specialist("Operations Manager", "Execute SQL actions if research and billing allow.", [check_patient_history, emergency_booking_tool])

        # Step 1: Research
        print("\n>> STEP 1: RESEARCHING SYMPTOMS")
        med_context = researcher.invoke({"input": user_input})['output']

        # Step 2: Insurance
        print("\n>> STEP 2: VERIFYING INSURANCE")
        bill_context = billing.invoke({"input": user_input})['output']

        # Step 3: Action
        print("\n>> STEP 3: EXECUTING CLINICAL ACTION")
        combined_input = f"User Query: {user_input}\nMedical: {med_context}\nBilling: {bill_context}"
        return ops.invoke({"input": combined_input})['output']