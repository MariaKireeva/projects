function numAdd(arg) {
    return function (arg2 = 4){
        let a = arg + arg2
        console.log(a)
    }
}
const func = numAdd(5);
func()