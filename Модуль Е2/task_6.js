let arr = [1, 1, 1,]
let counter = 1
if (arr.length === 1) {
    console.log('Массив состоит из одного элемента')
}
else {
    for (let i = 1; i < arr.length; i++) {
        if (arr[i - 1] === arr[i]) {
            counter += 1
        }
    }
}
if (counter != arr.length) {
    console.log('Элементы в массиве различны')
}
else {
    console.log('Все элементы в массиве одинаковы')
}