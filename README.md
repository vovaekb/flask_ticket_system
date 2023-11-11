# flask_ticket_system

⚔️ Simple Flask app for displaying player scores in game contest.
Setup and running

We need to install Redis server. Then install all necessary python packages using requirements.txt

```
pip install -r requirements.txt
```

Navigate to url http://127.0.0.1:5000/ in browser.

REST API endpoints:

    /contest_table (GET) - Returns html page with contest scores table.
    /score (POST) - add contest score in format of JSON: {"id": int, "score": float, "real_score": float}. returns 'Success'
