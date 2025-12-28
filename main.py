from email import message
import os
import argparse
from tabnanny import verbose
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
try:
    api_key = os.environ.get("GEMINI_API_KEY")
except:
    raise RuntimeError("api_key not found in env variables")


def main():
    print("Hello from ai-agent!")
    client = genai.Client(api_key=api_key)
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
    
    max_iterations = 20
    for iteration in range(max_iterations):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions], system_instruction=system_prompt
                ),
            )

            if response.usage_metadata == None:
                raise RuntimeError("failed API request")

            if args.verbose:
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

            for candidate in response.candidates:
                if candidate.content:
                    messages.append(candidate.content)

            # Check if model is finished (no function calls and has text response)
            has_function_calls = response.function_calls is not None and len(response.function_calls) > 0
            has_text_response = response.text is not None and response.text.strip() != ""

            if not has_function_calls and has_text_response:
                print("Final response:")
                print(response.text)
                break

            if response.function_calls:
                function_results = []
                for function_call in response.function_calls:
                    function_call_result = call_function(function_call, verbose=args.verbose)
                    
                    if not function_call_result.parts:
                        raise RuntimeError("Function call returned no parts")
                    
                    function_response = function_call_result.parts[0].function_response
                    if function_response is None:
                        raise RuntimeError("Function response is None")
                    
                    if function_response.response is None:
                        raise RuntimeError("Function response data is None")
                    
                    function_results.append(function_call_result.parts[0])
                    
                    if args.verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")

                if function_results:
                    messages.append(types.Content(
                        role="user",
                        parts=function_results
                    ))

        except Exception as e:
            print(f"Error during iteration {iteration + 1}: {e}")
            raise


if __name__ == "__main__":
    main()
