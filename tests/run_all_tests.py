import subprocess
import pathlib

ROOT = pathlib.Path(__file__).parent

print()

print("=" * 50)
print("TRADDERBOT TEST SUITE")
print("=" * 50)

for test in sorted(ROOT.rglob("test_*.py")):

    if test.name == "run_all_tests.py":
        continue

    print(f"\nRunning {test.relative_to(ROOT)}")

    subprocess.run(["python", str(test)])

print("\nAll tests completed.")