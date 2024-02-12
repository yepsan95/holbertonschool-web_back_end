import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    this._brand = brand;
    this._motor = motor;
    this._color= color;
    this._range = range;
  }

  cloneCar() {
    const ParentClassConstructor = Object.getPrototypeOf(this).constructor;
    return new ParentClassConstructor(this._brand, this._motor, this._color);
  }
}
