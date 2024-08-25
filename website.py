from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# First format HTML template with minimal and modern style
html_template_1 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ roll_number }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 500px;
            margin: 50px auto;
            padding: 20px;
            background: #ffffff;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #004085;
            margin-bottom: 20px;
        }
        label {
            font-weight: bold;
            margin-bottom: 5px;
            display: block;
        }
        .form-group {
            margin-bottom: 15px;
        }
        textarea, select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
            background-color: #f8f9fa;
            color: #495057;
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #004085;
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 18px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #002752;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            background: #e9ecef;
            border-radius: 5px;
            font-size: 16px;
            color: #212529;
            white-space: pre-wrap;
        }
        footer {
            margin-top: 30px;
            text-align: center;
            font-size: 14px;
            color: #6c757d;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Data Processor</h1>
        <form id="dataForm">
            <div class="form-group">
                <label for="jsonInput">JSON Input</label>
                <textarea id="jsonInput" placeholder='Enter JSON like {"data": ["A","1","b","2"]}'></textarea>
            </div>
            <div class="form-group">
                <label for="filter">Filter Type</label>
                <select id="filter">
                    <option value="all">All</option>
                    <option value="numbers">Numbers</option>
                    <option value="alphabets">Alphabets</option>
                    <option value="highest_lowercase_alphabet">Highest Lowercase Alphabet</option>
                </select>
            </div>
            <button type="submit">Submit</button>
        </form>
        <div class="result" id="result"></div>
    </div>
    <footer>
        &copy; 2024 Your Name. All rights reserved.
    </footer>

    <script>
        document.getElementById('dataForm').addEventListener('submit', function(e) {
            e.preventDefault();
            let jsonInput = document.getElementById('jsonInput').value;
            let filter = document.getElementById('filter').value;
            fetch('/bfhl', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: jsonInput
            })
            .then(response => response.json())
            .then(data => {
                let result = '';
                if (filter === 'numbers') {
                    result = 'Filtered Response\\nNumbers: ' + JSON.stringify(data.numbers, null, 2);
                } else if (filter === 'alphabets') {
                    result = 'Filtered Response\\nAlphabets: ' + JSON.stringify(data.alphabets, null, 2);
                } else if (filter === 'highest_lowercase_alphabet') {
                    result = 'Filtered Response\\nHighest Lowercase Alphabet: ' + JSON.stringify(data.highest_lowercase_alphabet, null, 2);
                } else {
                    result = 'Filtered Response\\n' + JSON.stringify(data, null, 2);
                }
                document.getElementById('result').textContent = result;
            })
            .catch(error => {
                document.getElementById('result').textContent = 'Error: ' + error;
            });
        });
    </script>
</body>
</html>
"""

# Second format HTML template with vibrant and bold style
html_template_2 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ roll_number }}</title>
    <style>
        body {
            font-family: 'Verdana', sans-serif;
            background-color: #333;
            color: #eee;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 30px;
            background: #444;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
        }
        h1 {
            text-align: center;
            color: #ff9800;
            margin-bottom: 40px;
        }
        label {
            font-weight: bold;
            margin-bottom: 10px;
            display: block;
            color: #ff9800;
        }
        .form-group {
            margin-bottom: 25px;
        }
        textarea, select {
            width: 100%;
            padding: 15px;
            border: 2px solid #ff9800;
            border-radius: 8px;
            font-size: 16px;
            background-color: #555;
            color: #fff;
        }
        button {
            width: 100%;
            padding: 15px;
            background-color: #ff5722;
            border: none;
            border-radius: 8px;
            color: white;
            font-size: 18px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #e64a19;
        }
        .result {
            margin-top: 30px;
            padding: 20px;
            background: #555;
            border-radius: 10px;
            font-size: 16px;
            color: #ff9800;
            white-space: pre-wrap;
            border: 2px solid #ff9800;
        }
        footer {
            margin-top: 50px;
            text-align: center;
            font-size: 14px;
            color: #bbb;
            background-color: #222;
            padding: 15px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Data Processor</h1>
        <form id="dataForm">
            <div class="form-group">
                <label for="jsonInput">JSON Input</label>
                <textarea id="jsonInput" placeholder='Enter JSON like {"data": ["A","1","b","2"]}'></textarea>
            </div>
            <div class="form-group">
                <label for="filter">Filter Type</label>
                <select id="filter">
                    <option value="all">All</option>
                    <option value="numbers">Numbers</option>
                    <option value="alphabets">Alphabets</option>
                    <option value="highest_lowercase_alphabet">Highest Lowercase Alphabet</option>
                </select>
            </div>
            <button type="submit">Submit</button>
        </form>
        <div class="result" id="result"></div>
    </div>
    <footer>
        &copy; 2024 Your Name. All rights reserved.
    </footer>

    <script>
        document.getElementById('dataForm').addEventListener('submit', function(e) {
            e.preventDefault();
            let jsonInput = document.getElementById('jsonInput').value;
            let filter = document.getElementById('filter').value;
            fetch('/bfhl', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: jsonInput
            })
            .then(response => response.json())
            .then(data => {
                let result = '';
                if (filter === 'numbers') {
                    result = 'Filtered Response\\nNumbers: ' + JSON.stringify(data.numbers, null, 2);
                } else if (filter === 'alphabets') {
                    result = 'Filtered Response\\nAlphabets: ' + JSON.stringify(data.alphabets, null, 2);
                } else if (filter === 'highest_lowercase_alphabet') {
                    result = 'Filtered Response\\nHighest Lowercase Alphabet:
