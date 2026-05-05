from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

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

INPUT_DIR = Path("voice_scripts")
OUTPUT_DIR = Path("voice_output")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

filename = input("Paste text file name, for example 01_mwd_short.txt: ").strip()

if not filename:
    raise RuntimeError("No filename was provided.")

input_path = INPUT_DIR / filename

if not input_path.exists():
    raise FileNotFoundError(f"File not found: {input_path.resolve()}")

if input_path.suffix.lower() != ".txt":
    raise RuntimeError("Input file must be a .txt file.")

text = input_path.read_text(encoding="utf-8").strip()

if not text:
    raise RuntimeError(f"The file is empty: {input_path.resolve()}")

output_path = OUTPUT_DIR / f"{input_path.stem}.mp3"

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