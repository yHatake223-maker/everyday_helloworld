import subprocess
import sys


def test_module_run():
    result = subprocess.run(
        [sys.executable, "-m", "everyday_helloworld"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "Hello, World!"
