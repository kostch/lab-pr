z = 0
let result = []
Min(z)
function Min(i){
    for(a = i; -100 <= a ; a--) {
        let b = a + 10
        console.log(getRandomIntInclusive(a, b))
        result.unshift(getRandomIntInclusive(a,b))
    }
}
C(0)
function Get(i) {
    for(a = i; 100 > a ; a++) {
        let b = a + '10'
        console.log(getRandomIntInclusive(a, b))
        C(i)
    }
    Min(a)
}

function Las(i) {
    a = i
    a = parseInt(a);
    let b = a + 10
    let res = result.shift()
    console.log(res + getRandomIntInclusive(a, b))
    let f = getRandomIntInclusive(a,b)
    console.log(getRandomIntInclusive(a,b), 'tets getrandom')
    let fe = res + f
    result.unshift(fe)
    C(i)
//    Min(a)
}

function getRandomIntInclusive(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min; //Максимум и минимум включаются
}

function C(i){
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    rl.question('Представляем что это крутилка которая, например, добавляет или убавляет обороты, поэтому пишем число либо положительное, либо отрицательное ', (answer) => {
        // TODO: Log the answer in a database
        rl.close();
        console.log(`Результат регулирования: ${Las(answer)}`);
    });
}
