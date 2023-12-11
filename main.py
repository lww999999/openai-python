import os


from openai import OpenAI
from openai.types import model

if __name__ == '__main__':

    client = OpenAI(
        api_key='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'
    )

    completion = client.completions.create(model='curie')
    print(completion.choices[0].text)
    print(dict(completion).get('usage'))
    print(completion.model_dump_json(indent=2))
