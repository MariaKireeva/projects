let arr = [null, 6, 8, 11, 0, true, 0, false, 66, 1];
let even_num = 0;
let odd_num = 0;
let zero_num = 0
for (let i = 0; i < arr.length; i++) {
    if (typeof arr[i] != "number") {

    }
    else if(arr[i] == 0) {
        zero_num += 1
    }
    else if (arr[i] % 2 === 0) {
        even_num += 1
    }
    else if (arr[i] % 2 === 1) {
        odd_num += 1
    }
}
console.log(` четных чисел -${even_num},\n нечетных чисел- ${odd_num},\n нулей - ${zero_num}`)