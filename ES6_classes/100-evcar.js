import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  cloneCar() {
    const parentClassName = Object.getPrototypeOf(this).constructor.name;
    const classConstructor = new Function(`return ${parentClassName}`);
    return new classConstructor();
  }
}
