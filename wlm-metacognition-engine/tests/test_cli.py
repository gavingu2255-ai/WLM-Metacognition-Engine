import json
import subprocess
import sys
from pathlib import Path


def test_cli_analyze(tmp_path):
    input_text = "A implies B. B implies C."
    input_file = tmp_path / "input.txt"
    input_file.write_text(input_text)

    result = subprocess.run(
        [sys.executable, "-m", "wlm_metacognition_engine.cli", "analyze", str(input_file)],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0

    output = json.loads(result.stdout)
    assert output["steps"] == ["A implies B", "B implies C"]
