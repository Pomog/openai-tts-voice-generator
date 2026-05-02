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
pip install -r requirements.txt
cp .env.example .env
eof
