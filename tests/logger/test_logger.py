from app.logger.logger import Logger

learning = Logger.get("LearningEngine")
execution = Logger.get("ExecutionManager")

learning.info("Learning Complete")
execution.info("Trade Executed")

print()
print("✓ TEST PASSED")