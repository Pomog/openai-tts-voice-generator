# OpenAI TTS Voice Generator

A small Python project for generating MP3 voice-over files from text scripts using the OpenAI Text-to-Speech API.

I created this for EVE Online video guides, but it can be reused for any tutorial or YouTube voice-over.

## Features

- Reads text files from `scripts/`
- Generates MP3 files into `output/`
- Uses `.env` for the OpenAI API key
- Keeps secrets and generated audio out of GitHub

## Setup

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Create .env from the example:
```bash
cp .env.example .env
```
Edit .env and add your real API key:
```
OPENAI_API_KEY=your_api_key_here
OPENAI_TTS_MODEL=gpt-4o-mini-tts
OPENAI_TTS_VOICE=cedar
```

## Usage
Add .txt scripts into the scripts/ folder.
```bash
python generate_tts.py
```
Generated MP3 files will appear in:
output/

## Security note

Do not commit .env.