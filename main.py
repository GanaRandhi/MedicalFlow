from src.agents import MedFlowOrchestrator
from dotenv import load_dotenv
import os

# Load the API key from the .env file
load_dotenv()

def main():
    # Verification check
    if not os.getenv("OPEN_ROUTER_KEY"):
        print("ERROR: OpenRouter API Key not found. Please check your .env file.")
        return

    system = MedFlowOrchestrator()
    
    query = "I am Gana. I have chest pain after my surgery. Does my Premium-Plus plan cover an ER visit?"
    
    print("--- MEDFLOW MULTI-AGENT SYSTEM STARTING ---")
    response = system.run(query)
    
    print("\n--- FINAL SYSTEM REPORT ---")
    print(response)

if __name__ == "__main__":
    main()