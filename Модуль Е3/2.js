let num = prompt('Введите число');
num = +num;
function checkPrime(){
    for (let i = 2; i <= num; i++){
        if (num % i === 0) {
            console.log('Это составное число')
            return
        }
        else {
            console.log('Это простое число')
            return
        }
    }
}
if (typeof num === 'number'){
    if(num > 1000){
        console.log('Вы ввели число большее 1000')
    }
    else if(num < 2){
        console.log('Нужно вводить числа, большие единицы')
    }
    else {
        checkPrime()
    }
}
else {
    console.log('Вы ввели не число')
}