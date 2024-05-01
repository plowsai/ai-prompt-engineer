import requests
import anthropic

ANTHROPIC_API_KEY = "YOUR API KEY"  # Replace with your Anthropic API key
OCTO_API_KEY = "YOUR API KEY" # Replace with your OctoAI API key

client = anthropic.Anthropic(
    api_key=ANTHROPIC_API_KEY,
)

original_instruct_prompt = """write an essay about frogs""" ## place your prompt to convert here

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.4,
    system="Given a prompt designed for an assistant model, convert it to be used with a base model. Use code as a trick to do this well.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Prompt to convert:\n\nApril 8, 2024 — Cohere recently announced the launch of Command R+, a cutting-edge addition to its R-series of large language models (LLMs). In this blog post, Cohere CEO Aidan Gomez delves into how this new model is poised to enhance enterprise-grade AI applications through enhanced efficiency, accuracy, and a robust partnership with Microsoft Azure.\nToday, we’re introducing Command R+, our most powerful, scalable large language model (LLM) purpose-built to excel at real-world enterprise use cases. Command R+ joins our R-series of LLMs focused on balancing high efficiency with strong accuracy, enabling businesses to move beyond proof-of-concept, and into production with AI.\nCommand R+, like our recently launched Command R model, features a 128k-token context window and is designed to offer best-in-class:\nAdvanced Retrieval Augmented Generation (RAG) with citation to reduce hallucinations\nMultilingual coverage in 10 key languages to support global business operations\nTool Use to automate sophisticated business processes\nOur latest model builds on the key strengths of Command R and further improves performance across the board. Command R+ outperforms similar models in the scalable market category, and is competitive with significantly more expensive models on key business-critical capabilities. We achieve this while providing the same commitment to data privacy and security that we’re known for.\nAs we continue to serve the global enterprise community, we are proud to announce a new collaboration with Microsoft Azure to accelerate enterprise AI adoption.\n“The collaboration with Cohere underscores our dedication to leading the charge in the AI revolution, bringing the innovative Command R+ model to Azure AI,” said John Montgomery, CVP of Azure AI Platform at Microsoft. “This partnership exemplifies our commitment to providing a comprehensive suite of AI tools that empower businesses to achieve more while adhering to the highest standards of security and compliance. Together, we’re setting new benchmarks for what’s possible in enterprise AI, fostering a future where technology amplifies human capability and innovation.”\n--\nGive me three good headlines\n"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "\nimport ai\n\ndef generate_headlines(press_release):\n  prompt = f\"\"\"Given the following press release, generate a Python list containing three compelling, informative headlines for a news article or blog post covering this announcement. \n\n  Each headline should:\n  - Be no more than 20 words \n  - Capture the key points about the new Command R+ model and Cohere's partnership with Microsoft Azure\n\n  Press Release:\n  \\"\\"\\"{press_release}\\"\\"\\"\n  \n  Respond with the Python list containing the three headlines, with each headline surrounded by double quotes.\"\"\"\n\n  return ai.generate(prompt)\n\npress_release = \"\"\"\nApril 8, 2024 — Cohere recently announced the launch of Command R+, a cutting-edge addition to its R-series of large language models (LLMs). In this blog post, Cohere CEO Aidan Gomez delves into how this new model is poised to enhance enterprise-grade AI applications through enhanced efficiency, accuracy, and a robust partnership with Microsoft Azure.\n\nToday, we're introducing Command R+, our most powerful, scalable large language model (LLM) purpose-built to excel at real-world enterprise use cases. Command R+ joins our R-series of LLMs focused on balancing high efficiency with strong accuracy, enabling businesses to move beyond proof-of-concept, and into production with AI.\n\nCommand R+, like our recently launched Command R model, features a 128k-token context window and is designed to offer best-in-class:\n\nAdvanced Retrieval Augmented Generation (RAG) with citation to reduce hallucinations\nMultilingual coverage in 10 key languages to support global business operations \nTool Use to automate sophisticated business processes\nOur latest model builds on the key strengths of Command R and further improves performance across the board. Command R+ outperforms similar models in the scalable market category, and is competitive with significantly more expensive models on key business-critical capabilities. We achieve this while providing the same commitment to data privacy and security that we're known for.\n\nAs we continue to serve the global enterprise community, we are proud to announce a new collaboration with Microsoft Azure to accelerate enterprise AI adoption.\n\n\"The collaboration with Cohere underscores our dedication to leading the charge in the AI revolution, bringing the innovative Command R+ model to Azure AI,\" said John Montgomery, CVP of Azure AI Platform at Microsoft. \"This partnership exemplifies our commitment to providing a comprehensive suite of AI tools that empower businesses to achieve more while adhering to the highest standards of security and compliance. Together, we're setting new benchmarks for what's possible in enterprise AI, fostering a future where technology amplifies human capability and innovation.\"\n\"\"\"\n\nprint(generate_headlines(press_release))\n\nOutput:\n\"\"\"\n[\n"
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Prompt to convert:\n\nSpend Less Time in Bird Library\nMake this shorter.\n"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "\nimport ai\n\ndef shorten_text(input_text):\n  prompt = f\"\"\"Shorten the following text while preserving the key meaning. Ensure the text you generate is shorter than the original:\n\n  Text: \"{input_text}\"\n  \n  Respond with the shortened text string inside quotes.\"\"\"\n\n  return ai.generate(prompt)\n\ntext = \"Spend Less Time in Bird Library\"\n\nprint('The shortened text is: ', shorten_text(input_text))\n\nOutput:\n\"\"\"\n\nThe shortened text is: \", \"\n"
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Prompt to convert:\n\npip uninstall -y transformers && pip uninstall -y flash-attn && pip install flash-attn && pip install git+https://github.com/huggingface/transformers && git clone https://github.com/OpenAccess-AI-Collective/axolotl && cd axolotl && pip3 install -e .[flash-attn] && pip3 install -U git+https://github.com/huggingface/peft.git && pip uninstall -y deepspeed && pip install -U deepspeed && pip install accelerate && pip uninstall -y deepspeed && pip install deepspeed==0.13.1 && conda install --name py3.10 mpi4py\nHow do I run this but use the specific branch dbrx of axolotl?\n"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "\nimport ai\n\ndef modify_commands(commands):\n  prompt = f\"\"\"Given the following series of shell commands:\n\n  ```\n  {commands}\n  ```\n  \n  Modify the commands to clone the specific 'dbrx' branch of the 'axolotl' repository instead of the default branch.\n\n  Respond with the updated series of commands.\"\"\"\n\n  return ai.generate(prompt)\n\ncommands = \"\"\"\npip uninstall -y transformers && pip uninstall -y flash-attn && pip install flash-attn && pip install git+https://github.com/huggingface/transformers && git clone https://github.com/OpenAccess-AI-Collective/axolotl && cd axolotl && pip3 install -e .[flash-attn] && pip3 install -U git+https://github.com/huggingface/peft.git && pip uninstall -y deepspeed && pip install -U deepspeed && pip install accelerate && pip uninstall -y deepspeed && pip install deepspeed==0.13.1 && conda install --name py3.10 mpi4py\n\"\"\"\n\nprint(modify_commands(commands))\n\nOutput:\n\"\"\"\n"
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Prompt to convert:\n\n{original_instruct_prompt.strip()}\n"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": ""
                }
            ]
        },
    ]
)
converted_prompt = message.content[0].text.split('')[0].strip()

print(converted_prompt)

def generate_octo(prompt, max_tokens, temperature):
  url = "https://text.octoai.run/v1/completions"
  headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {OCTO_API_KEY}"
  }
  data = {
      "model": "mixtral-8x22b",
      "prompt": prompt,
      "max_tokens": max_tokens,
      "temperature": temperature,
  }

  response = requests.post(url, headers=headers, json=data)

  if response.status_code == 200:
      result = response.json()
  else:
      print(f"Request failed with status code: {response.status_code}")
      print(f"Error message: {response.text}")

  return response.json()['choices'][0]['text']

print(generate_octo(converted_prompt, 500, .6).strip())