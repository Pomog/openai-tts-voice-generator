from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI


# Folder where this Python script is located: scripts/
BASE_DIR = Path(__file__).resolve().parent

# Project root folder: one level above scripts/
PROJECT_ROOT = BASE_DIR.parent

# Load .env from project root
load_dotenv(PROJECT_ROOT / ".env")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY was not found. Check your .env file.")

client = OpenAI(api_key=api_key)

MODEL = "gpt-4o-mini-tts"
VOICE = "cedar"

INSTRUCTIONS = """
Speak like a calm and clear EVE Online tutorial narrator.
Use a confident but beginner-friendly tone.
Do not speak too fast.
Pause slightly between important ideas.
"""

MANIFEST_FILE = BASE_DIR / "voice_manifest.txt"
OUTPUT_DIR = BASE_DIR / "voice_output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_manifest(manifest_path: Path) -> list[Path]:
    """
    Reads file paths from the manifest file.

    Empty lines are ignored.
    Lines starting with # are ignored.
    Paths are treated as relative to the scripts/ folder.
    """

    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest file not found: {manifest_path.resolve()}")

    files: list[Path] = []

    for line_number, line in enumerate(manifest_path.read_text(encoding="utf-8").splitlines(), start=1):
        line = line.strip()

        if not line:
            continue

        if line.startswith("#"):
            continue

        file_path = BASE_DIR / line

        if not file_path.exists():
            raise FileNotFoundError(
                f"File from manifest not found on line {line_number}: {file_path.resolve()}"
            )

        if file_path.suffix.lower() != ".txt":
            raise RuntimeError(
                f"Only .txt files are allowed. Problem on line {line_number}: {file_path.resolve()}"
            )

        files.append(file_path)

    if not files:
        raise RuntimeError(f"No text files found in manifest: {manifest_path.resolve()}")

    return files


def generate_voice(input_path: Path) -> Path:
    text = input_path.read_text(encoding="utf-8").strip()

    if not text:
        raise RuntimeError(f"The file is empty: {input_path.resolve()}")

    output_path = OUTPUT_DIR / f"{input_path.stem}.mp3"

    print("-" * 60)
    print(f"Generating voice from: {input_path}")
    print(f"Output file: {output_path}")

    with client.audio.speech.with_streaming_response.create(
        model=MODEL,
        voice=VOICE,
        input=text,
        instructions=INSTRUCTIONS.strip(),
        response_format="mp3",
    ) as response:
        response.stream_to_file(output_path)

    print(f"Saved: {output_path}")

    return output_path


def main() -> None:
    input_files = read_manifest(MANIFEST_FILE)

    print(f"Found {len(input_files)} text files in manifest.")
    print(f"Output folder: {OUTPUT_DIR.resolve()}")

    generated_files: list[Path] = []

    for input_file in input_files:
        output_file = generate_voice(input_file)
        generated_files.append(output_file)

    print("=" * 60)
    print("Done. Generated files:")

    for file in generated_files:
        print(f"- {file}")


if __name__ == "__main__":
    main()