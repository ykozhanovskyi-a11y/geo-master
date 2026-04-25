import os

# створюємо папки для стилів і скриптів
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)

files = {

"index.html": """<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<title>GeoMaster</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>

<h1>🌍 GeoMaster</h1>
<a href="game.html">Почати гру</a>

</body>
</html>
""",

"game.html": """<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<title>Гра</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>

<h2 id="question"></h2>
<div id="answers"></div>
<p>Бали: <span id="score">0</span></p>

<script src="js/data.js"></script>
<script src="js/score.js"></script>
<script src="js/game.js"></script>

</body>
</html>
""",

"css/style.css": """body {
font-family: Arial;
background: #1e3c72;
color: white;
text-align: center;
}

button{
padding:10px;
margin:10px;
cursor:pointer;
}
""",

"js/data.js": """const countries = [
{ name: "Україна", capital: "Київ" },
{ name: "Франція", capital: "Париж" },
{ name: "Німеччина", capital: "Берлін" },
{ name: "Італія", capital: "Рим" },
{ name: "Іспанія", capital: "Мадрид" }
];
""",

"js/score.js": """let score = 0;

function addPoint(){
score++;
document.getElementById("score").textContent = score;
}
""",

"js/game.js": """let current = 0;
let shuffled = countries.sort(() => 0.5 - Math.random());

function loadQuestion(){

if(current >= shuffled.length){
alert("Гру завершено! Бали: " + score);
location.reload();
return;
}

const country = shuffled[current];

document.getElementById("question").textContent =
"Яка столиця країни " + country.name + "?";

const answersDiv = document.getElementById("answers");
answersDiv.innerHTML = "";

let options = countries.map(c => c.capital)
.sort(() => 0.5 - Math.random())
.slice(0,4);

if(!options.includes(country.capital)){
options[0] = country.capital;
}

options.sort(() => 0.5 - Math.random());

options.forEach(option => {

const btn = document.createElement("button");
btn.textContent = option;

btn.onclick = function(){

if(option === country.capital){
addPoint();
}

current++;
loadQuestion();

};

answersDiv.appendChild(btn);

});

}

loadQuestion();
"""
}

# записуємо файли на диск
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Гра створена правильно!")