import openai
import streamlit as st
import requests

# Set up OpenAI API
openai.api_key = ''


# Chatbot function
def ask_chatgpt(question):
    prompt = f'User: {question}\nChatGPT:'

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    chatgpt_response = response.choices[0].text.strip().replace('ChatGPT:', '')
    return chatgpt_response

# OpenAI API call function for expert recommendations
def get_expert_recommendations(destination):
    # Ask ChatGPT for expert recommendations
    question = f"What are some expert recommendations for road trips in {destination}?"
    response = ask_chatgpt(question)
    recommendations = response.split('\n')

    return recommendations

# OpenAI API call function for personalized itineraries
def get_personalized_itineraries(destination, days_staying):
    # Ask ChatGPT for personalized itineraries
    question = f"Can you provide some personalized {days_staying}-day road trip itineraries for {destination}?"
    response = ask_chatgpt(question)
    itineraries = response.split('\n')

    return itineraries

# OpenAI API call function for convenient travel tools
def get_convenient_travel_tools(destination, budget):
    # Ask ChatGPT for convenient travel tools
    question = f"What are some convenient travel tools for a road trip to {destination} with a budget of {budget}?"
    response = ask_chatgpt(question)
    tools = response.split('\n')

    return tools

# Streamlit app
def main():
    st.title("Road Trip Planner")
    st.write("Empowering travelers with the ultimate road trip planning experience!")

    destination = st.text_input("Destination")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    budget = st.number_input("Budget")
    days_staying = (end_date - start_date).days if end_date > start_date else 0
    interests = st.text_input("Interests")

    if st.button("Generate Itinerary"):
        dates = [start_date, end_date]
        interests = interests.split(",") if interests else []
        
        itinerary = generate_itinerary(destination, dates, budget, interests)

        st.subheader("Itinerary:")
        for item in itinerary:
            st.write(item)

    st.markdown("---")
    st.subheader("Expert Recommendations")
    st.write("Discover expert recommendations for your road trip:")
    recommendations = get_expert_recommendations(destination)
    for recommendation in recommendations:
        st.markdown(f"<div style='font-size: 20px; white-space: pre-wrap;'>{recommendation}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Personalized Itineraries")
    st.write("Create personalized itineraries for your road trip:")
    itineraries = get_personalized_itineraries(destination, days_staying)
    for itinerary in itineraries:
        st.markdown(f"<div style='font-size: 20px; white-space: pre-wrap;'>{itinerary}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Convenient Travel Tools")
    st.write("Access convenient travel tools for a seamless road trip:")
    tools =get_convenient_travel_tools(destination, budget)
    for tool in tools:
       st.markdown(f"<div style='font-size: 20px; white-space: pre-wrap;'>{tools}</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
