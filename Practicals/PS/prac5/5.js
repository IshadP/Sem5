const body = document.getElementById("body");
const incbtn = document.getElementById("incbtn");
const decbtn = document.getElementById("decbtn");
const resbtn = document.getElementById("resbtn");
var text = document.createElement('p');
let fontsize = 10;

text.innerText = 'This is text';
text.style.fontSize = `${fontsize}px`;
body.appendChild(text);

resbtn.onclick = function(e) {
    e.preventDefault();
    fontsize = 10;
    text.style.fontSize = `${fontsize}px`;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function animateFontSize() {
    text.innerText = "Text is growing"
    text.style.color = "red";
    for (let i = fontsize; i <= 100; i += 1) {
        fontsize = i;
        text.style.fontSize = `${fontsize}px`;
        await sleep(100);
    }
    await animateFontSizedown();
}

async function animateFontSizedown(){
    text.innerText = "Text is shrinking";
    text.style.color = "blue"
    for (let i = fontsize; i >= 10; i -= 1) {
        fontsize = i;
        text.style.fontSize = `${fontsize}px`;
        await sleep(100);
    }
    await animateFontSize();
}

// Start the animation loop
animateFontSize();
