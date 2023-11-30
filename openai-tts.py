import argparse
from pathlib import Path
from openai import OpenAI

def main(model, voice, text, speech_file_path):
    client = OpenAI()

    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=text
    )

    response.stream_to_file(speech_file_path)
    print(f"Speech saved to {speech_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text to Speech using OpenAI API")
    
    # default param
    default_model = "tts-1"
    default_voice = "onyx"
    default_text = "Today is a wonderful day to build something people love!"
    default_path = Path(__file__).parent / "speech.mp3"

    # args list
    parser.add_argument("--model", default=default_model, help="Model to use for text to speech")
    parser.add_argument("--voice", default=default_voice, help="Voice to use for text to speech")
    parser.add_argument("--text", default=default_text, help="Text to convert to speech")
    parser.add_argument("--path", default=default_path, type=Path, help="Path to save the speech file")

    args = parser.parse_args()

    main(args.model, args.voice, args.text, args.path)
