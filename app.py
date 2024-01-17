from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS module
from YoutubeTags import videotags

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in your Flask app

@app.route('/get_video_tags', methods=['GET'])
def get_video_tags():
    link = request.args.get('link')

    if link is None:
        return jsonify({'error': 'Missing link parameter'}), 400

    try:
        tags = videotags(link)

        # Convert tags to a list if it's a comma-separated string
        if isinstance(tags, str):
            tags = [tag.strip() for tag in tags.split(',')]

        return jsonify({'tags': tags})
    except Exception as e:
        return jsonify({'error': f'Error retrieving tags: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
