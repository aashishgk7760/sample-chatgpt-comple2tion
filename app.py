from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv
import boto3

app = Flask(__name__)




# Set your OpenAI API key here (use an environment variable in production)
load_dotenv()  # Load environment variables from .env file

# os.environ['OPENAI_API_KEY'] = get_secret('openiapikey')
openai_api_key = os.environ.get("OPENAI_API_KEY")  # Replace 'your-api-key' with the actual key for local testing
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_resources():
    # Extract data from form
    cloud_provider = request.form.get('cloud_provider')
    experience = request.form.get('experience')
    interest = request.form.get('interest')

    try:
        # Using the OpenAI Chat API endpoint with GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Update to the latest GPT-4 turbo model
            messages=[
                {"role": "user", "content": f"I am interested in {interest}, have {experience} years of experience and prefer {cloud_provider} cloud services. What resources do you recommend?"}
            ]
        )
        # Assuming the last message is the AI's response
        recommendations = response['choices'][0]['message']['content']
        recommendations_list = recommendations.split('\n')
    except openai.error.OpenAIError as e:
        recommendations_list = [f"An error occurred: {str(e)}"]

    # Pass the recommendations list to the template
    return render_template('results.html', recommendations=recommendations_list)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80 , debug=True)







