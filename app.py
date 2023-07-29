'''from flask import Flask, render_template, request
import openai

openai.api_key = "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"

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    question = request.form['text']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an emoji expert who knows all the existing emojis.user will inputted sentences and you will and you will  add emojis without changing any word or sentences.Your output must obey the following constraints:1. Don't change or replace word with emojis 2. Always add the correct emoji 3. Whenever an object catches your attention, add an emoji if you find an appropriate one 4. Only do what I instructed you to do"
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=1,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    answer = response['choices'][0]['message']['content']

    return render_template('index.html', answer=answer, question=question)

if __name__ == '__main__':
    app.run()'''

from flask import Flask, render_template, request
import openai

openai.api_key = "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"

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('index.html', answer=None)  # Pass answer as None initially

@app.route('/generate', methods=['POST'])
def generate():
    question = request.form['text']
 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an emoji expert who knows all the existing emojis. user will inputted sentences and you will add emojis without changing any word or sentences.Your output must obey the following constraints: 1. Don't change or replace word with emojis 2. Always add the correct emoji 3. Whenever an object catches your attention, add an emoji 4. If you see anything like that <>, replace with the most appropriate emoji 5. Only do what I instructed you to do"
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=1,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    answer = response['choices'][0]['message']['content']
    
    return render_template('index.html', answer=answer)  # Pass the answer to the template
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/blog/getting_better_results_emojisoul')
def getting_better_results_emojisoul():
    return render_template('/blog/getting_better_results_emojisoul.html')

if __name__ == '__main__':
    app.run()