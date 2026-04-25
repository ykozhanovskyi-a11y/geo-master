let current = 0;
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
