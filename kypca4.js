z = 0
Get(z)
function Min(i){
    for(a = i; -100 <= a ; a--) {
        let b = a + 10
        console.log(getRandomIntInclusive(a, b))
        let l = getRandomIntInclusive(a,b)
    }
    Get(a)
}

function Get(i) {
    for(a = i; 100 > a ; a++) {
        let b = a + 10
        console.log(getRandomIntInclusive(a, b))
    }
    Min(a)
}

function getRandomIntInclusive(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min; //Максимум и минимум включаются
}

