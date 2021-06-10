function ElectroDevice(deviceName, isTurnedOn, power){
    this.isTurnedOn = isTurnedOn;
    this.power = power;
    this.deviceName = deviceName
}
function Fridge(company,color) {
    this.company = company;
    this.color = color;
    this.getInfo = function (){
        console.log(this.deviceName + ' ' + 'color is ' + this.color)
    }
}
function Phone(brandName, memory) {
    this.brandName = brandName
    this.memory = memory
    this.getInfo = function (){
        console.log(this.deviceName +' '+'memory is ' + this.memory)
    }
}

Fridge.prototype = new ElectroDevice('Fridge', true, 100)
const fridge = new Fridge('samsung','white')
Phone.prototype = new ElectroDevice('Phone', false, 60)
const pixel = new Phone('Pixel', 200)

console.log(fridge)
fridge.getInfo()
console.log(pixel)
pixel.getInfo()