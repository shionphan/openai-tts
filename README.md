## Description

This is a tool developed using the API provided by OpenAI, originating from OpenAI API's Text to Speech interface. The code was also generated by ChatGPT, I hope it can be of help to you.

## How to Use:

* Install the OpenAI Python library and set the API key in your environment variables
* Users can run this script from the command line and have the option to specify these parameters.
* For example, execute `python openai-tts.py --model "tts-1" --voice "alloy" --text "Hello, world!" --path "/path/to/speech.mp3"`.
* If the user does not specify any parameters, the script will use the default values.

## Note:

* Before you start, you need to read the OpenAI API documentation (https://platform.openai.com/docs/quickstart?context=python) and set the API key in your environment variables.
* Ensure that you have installed the `argparse`` library, which is part of the Python standard library and is used for parsing command-line arguments.
* I have used the Path type for handling file paths, which helps ensure compatibility across different platforms.