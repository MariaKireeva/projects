function makeObj(){
    return Object.create(null, {})
}
newObj = makeObj()
console.log(newObj.constructor)