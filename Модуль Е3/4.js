let a = 4
let b = 14
const countNumber = setInterval(function (){
    console.log(a+=1)
}, 1000)
setTimeout(function (){
    clearInterval(countNumber)
}, (b - a + 1) * 1000)