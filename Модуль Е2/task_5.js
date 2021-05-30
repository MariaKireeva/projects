let arr = [5, 7, 88, 17,'fox','true']
let arr_l = arr.length
console.log('Длина массива-'+ arr_l)
let result = arr.map(function(item, index, array) {
    console.log(item)
});