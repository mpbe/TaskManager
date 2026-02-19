from app import create_app

"""
running the main flask app
"""

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)