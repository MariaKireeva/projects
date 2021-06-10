let obj = {
    'a': 1,
    b: 2,
    c: 3,
    d: 4,
}
function iterFunction(string, obj){
    return !!obj[string];

}
a = iterFunction('a', obj)
console.log(a)