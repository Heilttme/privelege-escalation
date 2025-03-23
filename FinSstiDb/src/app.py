from flask import Flask, request, render_template_string

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def filtered(template):
    blacklist = ["self.__dict__", "config", "url_for", "../", "process", 
                 "cat", "less", "more", "head", "tail", "strings", "tac", "awk", "grep", "sort", "find", "read"]

    for b in blacklist:
        if b in template:
            return "Blocked: Suspicious input detected!"

    return template

@app.route("/")
def index():
    return """
    <html>
    <head>
        <title>Customer Reviews</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                text-align: center;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 20px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                margin-top: 50px;
                border-radius: 10px;
            }
            h1 {
                color: #333;
            }
            textarea, input {
                width: 100%;
                padding: 10px;
                margin-top: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            button {
                background: #28a745;
                color: white;
                border: none;
                padding: 12px;
                width: 100%;
                font-size: 18px;
                border-radius: 5px;
                cursor: pointer;
                margin-top: 10px;
            }
            button:hover {
                background: #218838;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Leave a Review</h1>
            <p>Share your experience with us!</p>
            <form action="/review" method="GET">
                <input type="text" name="name" placeholder="Your Name" required><br>
                <textarea name="review" placeholder="Write your review here..." required></textarea><br>
                <button type="submit">Submit Review</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route("/review")
def review():
    name = request.args.get("name", "Anonymous")
    review = request.args.get("review", "No review provided.")

    safe_name = filtered(name)

    template = f"""
    <html>
    <head>
        <title>Review Submitted</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                text-align: center;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 20px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                margin-top: 50px;
                border-radius: 10px;
            }}
            h1 {{
                color: #333;
            }}
            .review-box {{
                background: #e9ecef;
                padding: 15px;
                border-radius: 5px;
                margin-top: 20px;
                font-size: 16px;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                text-decoration: none;
                color: #007bff;
                font-size: 16px;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Thank you, <b>{safe_name}</b>!</h1>
            <p>We appreciate your feedback.</p>
            <div class="review-box">
                <p>{review}</p>
            </div>
            <br>
            <a href="/">Submit another review</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

