let a = 5
if (typeof a === 'number'){
    console.log(a + '- число')
}  else if (typeof a === 'string' ){
    console.log(a + '- строка')
}  else if (typeof a === 'boolean'){
    console.log( a + '- булевый тип')
}  else {
    console.log('Тип не определен.')
}
