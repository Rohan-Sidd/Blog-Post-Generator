
#streamlit for frontend

import streamlit as st

import pyperclip

#Using Google Gemini
import google.generativeai as genai

#openAI for image generation


from openai import OpenAI

from apikey import api_key





#from apikey import google_gemini_api_key

genai.configure(api_key=api_key)

# client=OpenAI(api_key=api_key)



generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

system_instruction = "\n"

#setting up the gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)





emoji_map = {
    250: "😀",
    500: "😳",
    750: "😠",
    1000: "🤬"
}

word_map={
    1:"Nice",
    2:"Okayyy",
    3:"Broo!!",
    4:"Wtf! Stop man",
    5:"Nee amma"
}

#set app to wide mode
st.set_page_config(layout="wide")

#title of app

st.title('👾🤖 Optimus Prime writes your blogs!')

st.subheader("Welcome human! I'm Optimus and with my knowledge I can help you!")


#sidebar for user prompt
with st.sidebar:
    st.title("Gimme your blog details human!")
    st.subheader("Specify the details and I'll do the rest!")

   

    #Blog title
    blog_title=st.text_input("Blog Title")

    #keywords input
    keywords=st.text_area("Enter comma separated keywords")

    #number of words
    num_words = st.slider("Number of Words", min_value=250, max_value=1000, step=250, format="%.0f", key="slider")
    st.write(f'<span style="font-size: 30px;">{emoji_map[num_words]}</span>', unsafe_allow_html=True)

    #number of images
    num_images=st.number_input("Number of Images",min_value=1, max_value=5, step=1)
    st.write(f'<span style="font-size: 30px;">{word_map[num_images]}</span>', unsafe_allow_html=True)

    convo = model.start_chat(history=[
        {
            "role": "user",
            "parts": [f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative and maintains a consistent tone throughout."]
        },
        {
            "role": "model",
            "parts": ["## The Rise of Artificial Creativity: Exploring the Effects of Generative AI\n\nThe world of technology is abuzz with the potential of **Generative AI**, a subset of **Machine Learning applications** that goes beyond simply processing information – it creates. From composing music and writing poetry to designing stunning visuals and even generating realistic human faces, this **technology innovation** is blurring the lines between human and machine creativity. But as we marvel at the possibilities of **artificial creativity**, it's crucial to explore its **ethical implications** and potential **AI impact on society**.\n\nOne of the most prominent effects of Generative AI is its democratization of content creation. Tools powered by this technology are making it possible for anyone, regardless of their artistic skills, to express themselves creatively. Aspiring musicians can now compose symphonies, writers can overcome writer's block with AI-generated story prompts, and entrepreneurs can design logos and marketing materials without needing extensive design expertise. This accessibility opens doors for individuals and small businesses, fostering a new era of creative expression. \n\nHowever, this ease of creation also raises concerns. The ability to generate hyper-realistic images and videos, for example, could be misused to create deepfakes – fabricated media that can spread misinformation and damage reputations. Additionally, the question of ownership and copyright arises when AI generates content. If a machine creates a piece of music, who owns the rights to it? These **ethical implications** require careful consideration as Generative AI becomes increasingly integrated into our lives.\n\nBeyond the realm of creative expression, Generative AI is also making waves in various industries. In healthcare, it is being used to design new drugs and accelerate medical research. Architects are utilizing it to generate building layouts, and engineers are employing it for product design and optimization. The applications seem limitless, offering the potential to revolutionize numerous sectors and boost efficiency across the board.\n\nHowever, the widespread adoption of Generative AI also raises concerns about job displacement. As machines become increasingly capable of performing tasks that were once exclusive to humans, the workforce landscape could undergo significant transformations. It's essential to acknowledge these potential disruptions and proactively explore strategies for retraining and upskilling individuals whose jobs might be impacted.\n\nThe rise of Generative AI presents us with a double-edged sword. It's a tool with immense potential for positive impact, but it also comes with ethical challenges and societal implications that need to be addressed. As we move forward, fostering open discussions, establishing ethical guidelines, and prioritizing responsible development will be crucial to ensure that this **technology innovation** serves as a force for good in shaping the future of our society."]
        },
    ])

    submit_button=st.button("Generate Blog")
    convo.send_message("YOUR_USER_INPUT")

#if submit button is pressed
if submit_button:
        

        # response = client.images.generate(
        #       model="dall-e-3",
        #       prompt="a white siamese cat",
        #       size="1024x1024",
        #       quality="standard",
        #       n=1,
        #     )
        # image_url = response.data[0].url

        # st.image(image_url,caption="real image, not AI generated!")
        
        


        generated_blog = convo.last.text
        st.title("Your BLOG post:")
        st.write(generated_blog)
        st.write("Click below to copy the generated blog to clipboard:")
        if st.button("Copy to Clipboard"):
            pyperclip.copy(generated_blog)
            st.success("Copied to clipboard!")





