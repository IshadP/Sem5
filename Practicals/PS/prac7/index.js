const strdiv = document.getElementById("vowel");
const stri = document.getElementById("str");
const numdiv = document.getElementById("num");
const number = document.getElementById("number");
let str = document.getElementById('strinput').value;
let num = document.getElementById('numinput').value;
let submit = document.getElementById('submitbtn');

function findLastVowel(str){
let vowel = "AEIOUaeiou";
let strarr = str.split('')
console.log(strarr.length)
let final = 0;
let vow = '';
console.log(strarr)
for (let i = 0; i < strarr.length; i++) {
    if(vowel.includes(strarr[i])){
        final = i+1;
        vow = strarr[i];
        break;
    }
}
final = strarr.length - final + 1;
const para = document.createElement('td');
para.innerHTML = `${final}(${vow.toLowerCase()})`;
stri.append(para);
return 0;
}

function reverseNumber(num){
    let rev = num.toString().split('').reverse().join('');
    const pr = document.createElement('td');
    pr.innerHTML = rev;
    number.append(pr);
    return 0;
}

findLastVowel(str);
reverseNumber(num)


