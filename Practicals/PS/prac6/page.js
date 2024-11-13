const table = document.getElementById("tble");

function appendTableRow(num, sqr,cbe){
    let row = document.createElement('tr');
    let col1 = document.createElement('th')
    col1.classList.add("number")
    let col2 = document.createElement('th')
    let col3 = document.createElement('th')
    col2.classList.add("eq")
    col3.classList.add("eq")
    col1.innerText = num;
    col2.innerText = sqr;
    col3.innerText = cbe;
    row.append(col1);
    row.append(col2);
    row.append(col3);
    table.append(row)
}




for(let i = 0; i <=10; i++){
sqr = i*i;
cbe = i*i*i;
appendTableRow(i, sqr, cbe);
}