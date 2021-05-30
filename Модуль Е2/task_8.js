let fruits = new Map([

    ["apple", "red"],

    ["lemon", "yellow"],

    ["grape", "green"]

]);
for (let name of fruits.keys()) {

    console.log(`Ключ — ${name}, значение — ${fruits.get(name)}`);

}
