let num = +(prompt ('Введите число '))
let type_num = typeof num
let a = num % 2
if (isNaN(num)){
    console.log('Упс, кажется, вы ошиблись')
}

   else if (a == 0){
    console.log('Число четное')
}
else{
    console.log('Число нечетное')
}

