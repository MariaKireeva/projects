class ElectroDevice {
    constructor(deviceName, isTurnedOn, power) {
        this.isTurnedOn = isTurnedOn;
        this.power = power;
        this.deviceName = deviceName
    }
}
class Fridge extends ElectroDevice{
    constructor(company, color, deviceName, isTurnedOn, power) {
        super(deviceName, isTurnedOn, power);
        this.company = company;
        this.color = color;
        this.getInfo = function () {
            console.log(deviceName + ' ' + 'color is ' + this.color)
        }
    }
}
class Phone extends ElectroDevice{
    constructor(brandName, memory, deviceName, isTurnedOn, power) {
        super(deviceName, isTurnedOn, power);
        this.brandName = brandName;
        this.memory = memory;
        this.getInfo = function () {
            console.log(deviceName +' '+'memory is ' + this.memory)
        }
    }
}
const fridge = new Fridge('samsung', 'white', 'Fridge', true, 100)
const pixel = new Phone('pixel', 1000, 'Phone', false, 700)
console.log(fridge)
fridge.getInfo()
console.log(pixel)
pixel.getInfo()



