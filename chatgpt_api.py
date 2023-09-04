import openai

# main function from here
openai.api_key = "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"

def chat_with_chatgpt(prompt, model="text-davinci-003"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

if __name__ == "__main__":
    data_1 = chat_with_chatgpt("wWrite a  effictive but summarized under 200 words product description   of Peanut Butter for old  customer  wirh atleast  100 words , product details are MYFITNESS Chocolate Peanut Butter Smooth 1250g | 22g Protein | Tasty & Healthy Nut Butter Spread |Vegan| Dark Chocolate | Cholesterol Free, Gluten Free| Smooth Peanut Butter | Zero Trans Fat")
    print(data_1)