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
    const c = 10
    const add = (a, c) => a + c
    const sub = (a, c) => a - c
    const ops = [add, sub];
    const randOp = (a, c) => ops[Math.floor(Math.random() * ops.length)](a, c)
    let b = randOp(a,c)
    let res = result.shift()
    let f = getRandomIntInclusive(a,b)
    console.log('Результат регулирования: ', res + f)
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
        Las(answer)
    });
}
