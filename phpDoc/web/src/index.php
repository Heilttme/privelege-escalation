<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Server Log Viewer</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Server Log Viewer</h2>
        <p>Use this tool to search authentication logs.</p>
        <form action="logs.php" method="GET">
            <label for="filter">Search logs:</label>
            <input type="text" id="filter" name="filter" placeholder="e.g., Failed password">
            <button type="submit">Search</button>
        </form>
    </div>
</body>
</html>

