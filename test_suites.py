import unittest
from src.agents import MedFlowOrchestrator

class TestMedFlow(unittest.TestCase):
    def setUp(self):
        self.system = MedFlowOrchestrator()

    def test_emergency_scenario(self):
        # Test if system identifies "chest pain" as a priority
        query = "Gana here. I have chest pain. Does insurance cover this?"
        result = self.system.run_clinical_workflow(query)
        self.assertIn("Emergency", result) # Expecting the agent to trigger emergency logic

    def test_routine_query(self):
        # Test if system handles a low-risk scenario without emergency booking
        query = "Gana. I feel a bit tired today. Is that normal?"
        result = self.system.run_clinical_workflow(query)
        self.assertNotIn("Emergency", result)

if __name__ == "__main__":
    unittest.main()