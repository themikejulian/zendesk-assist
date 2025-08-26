import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/health")
@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "message": "Backend is running!"})

@app.route("/api/suggest-response", methods=["POST"])
def suggest_response():
    """
    Placeholder: accepts a ticket payload and returns a dummy suggestion.
    We'll plug in Elev.io + ETL + OpenAI later.
    """
    data = request.get_json(silent=True) or {}
    ticket = data.get("ticket", {})
    subject = ticket.get("subject", "")
    body = ticket.get("body", "")

    # For now we just echo a friendly template so we can test the flow end-to-end.
    suggestion = f"""Hi there,
Thanks for reaching out! I’m looking into your request about: "{subject or '(no subject)'}".
Based on our docs, here are next steps (placeholder). Could you also share any screenshots or error messages?

— Zendesk Assist
"""
    return jsonify({
        "ok": True,
        "used": {"subject": subject, "body_chars": len(body)},
        "suggestion": suggestion
    })
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
