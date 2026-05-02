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

scripts = {
    "01_intro.mp3": """
Hello capsuleers.

In this video, I will show how I complete Mission 49: Our Man Dagan
from the Sisters of EVE epic arc.

This mission is famous among new players because Dagan has a very strong tank.
Many beginner ships can damage him, but they cannot apply enough DPS to finish the job.

Today I am using a Cormorant destroyer with railguns and a light missile launcher.
This is not an expensive fit, around 5.2 million ISK,
but it has enough damage to complete the mission if you fly it correctly.

The most important lesson in this mission is simple:
your ship fit matters.
You need enough DPS, good ammo, and good range control.
""",

    "02_fit_section.mp3": """
This is the Cormorant fit I use for the mission.

It has seven 125 millimeter Prototype Gauss Guns,
one compact light missile launcher,
two Magnetic Field Stabilizers for extra turret damage,
and a basic shield tank.

The fit shows about 171 DPS,
which is enough for this mission.

The capacitor is not stable,
but that is acceptable because the fight should not last forever.

I use Caldari Navy Antimatter Charge S
for higher close-range railgun damage.

With this setup, I want to apply as much damage as possible
and finish Dagan before capacitor becomes a serious problem.
""",

    "03_fight.mp3": """
When you enter the mission pocket, do not panic.

First, check the enemies and start applying damage carefully.

The main target is Dagan,
but if smaller enemies are bothering you,
remove them first.

After that, focus all damage on Dagan.

Watch his shield carefully.

If his shield goes down and stays down,
your DPS is enough.

If his shield regenerates faster than you damage him,
your fit does not have enough applied DPS.

In that case, you need better ammo,
more damage modules,
better skills,
or help from another player.
"""
}

for filename, text in scripts.items():
    output_path = Path(filename)

    print(f"Generating {filename}...")

    with client.audio.speech.with_streaming_response.create(
        model=MODEL,
        voice=VOICE,
        input=text.strip(),
        instructions=INSTRUCTIONS.strip(),
        response_format="mp3",
    ) as response:
        response.stream_to_file(output_path)

    print(f"Saved: {output_path}")

print("Done. Three voice-over files generated.")