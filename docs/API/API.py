from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/text', methods=['POST'])
def receive_text():
    data = request.json  # Récupère les données JSON envoyées dans la requête
    text = data.get('text')  # Récupère la valeur du champ 'text'

    # Traitez le texte ou effectuez toute autre logique souhaitée
    # ...

    # Préparez la réponse JSON
    response = {
        'message': 'Text received',
        'processed_text': text.upper()  # Exemple : convertit le texte en majuscules
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
