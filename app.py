<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Passenger Demand Prediction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f8;
        }
        .container {
            width: 400px;
            margin: 80px auto;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
        }
        label {
            font-weight: bold;
        }
        input, select, button {
            width: 100%;
            padding: 8px;
            margin-top: 6px;
            margin-bottom: 15px;
        }
        button {
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .result {
            text-align: center;
            font-size: 18px;
            color: green;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Passenger Demand Prediction</h2>

    <label>Hour of Day</label>
    <input type="number" min="0" max="23" placeholder="Enter hour (0–23)">

    <label>Route ID</label>
    <input type="number" placeholder="Enter route ID">

    <label>Day Type</label>
    <select>
        <option>Weekday</option>
        <option>Weekend</option>
    </select>

    <button>Predict Passenger Demand</button>

    <div class="result">
        Predicted Passenger Count: —
    </div>
</div>

</body>
</html>
